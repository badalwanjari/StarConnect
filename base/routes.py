from datetime import datetime
from enum import Enum
import os
import secrets
from PIL import Image
from flask import jsonify, render_template, url_for, flash, redirect, request, abort
from base import app, db, bcrypt
from base.create_db import add_data, create_db
from base.forms import CampaignRegistrationForm, RegistrationForm, LoginForm, InfluencerRegistrationForm, SponsorRegistrationForm
from base.models import Campaign, Contract, Influencer, CampaignRequest, Sponsor, User
from flask_login import login_user, current_user, logout_user, login_required
from functools import wraps
from flask import abort


class Role(Enum):
    INFLUENCER = "INFLUENCER"
    SPONSOR = "SPONSOR"
    ADMIN = "ADMIN"


def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.role not in roles:
                flash("You are not authorized!")
                return redirect(url_for('/'))  
            return f(*args, **kwargs)
        return decorated_function
    return decorator

########################################33

# create_db(app, db)
# add_data(app, db)

###########################################
################UTILITY#####################
###########################################

@login_required
def save_picture(form_picture, folder_name):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, f'static\\{folder_name}\\' , picture_fn)
    if folder_name == "profile_pics":
        output_size = (125, 125)
    else:
        output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn




###########################################
################USER#####################
###########################################

@app.route("/")
@app.route("/home")
def home():
    campaigns = []
    query_campaigns = None

    if current_user.is_authenticated and current_user.role == Role.SPONSOR:
        query_campaigns = Campaign.query.filter_by(sponsor_id=current_user.sponsor.id).all()
    else:
        query_campaigns = Campaign.query.filter_by(is_disabled=False).all()
    
    for campaign in query_campaigns:
        image_file = url_for('static', filename='campaign_poster/' + campaign.image_file)
        campaigns.append({"image": image_file,"campaign": campaign, "sponsor": Sponsor.query.filter_by(id=campaign.sponsor_id).first()})

    
    

    return render_template('index.html', campaigns=campaigns)




@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        
        if (form.is_company.data == True):
            user.role = Role.SPONSOR  
        else:
            user.role = Role.INFLUENCER

        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.html', title='Register', form=form)




@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if current_user.is_disabled:
                if current_user.role == Role.INFLUENCER:
                    return redirect(url_for('influencer_account_edit'))
                else:
                    return redirect(url_for('sponsor_account_edit'))
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('auth/login.html', title='Login', form=form)




@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))





@login_required
@role_required(Role.INFLUENCER)
@app.route("/influencer-account", methods=['GET', 'POST'])
def influencer_account_edit():
    form = InfluencerRegistrationForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data

        influencer = current_user.influencer
        if influencer is None:
            influencer = Influencer(
                user_id=current_user.id, 
                influencer_name=form.name.data, 
                category=form.category.data, 
                niche=form.niche.data, 
                reach=form.reach.data, 
                profile_url=form.profile_url.data, 
                bio=form.bio.data
            )
            current_user.is_disabled = False
            db.session.add(influencer)
        else:
            influencer.influencer_name = form.name.data
            influencer.category = form.category.data
            influencer.niche = form.niche.data
            influencer.reach = form.reach.data
            influencer.profile_url = form.profile_url.data
            influencer.bio = form.bio.data

        if form.picture.data:
            picture_file = save_picture(form.picture.data, "profile_pics")
            current_user.image_file = picture_file

        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        if current_user.influencer:
            form.name.data = current_user.influencer.influencer_name
            form.category.data = current_user.influencer.category
            form.niche.data = current_user.influencer.niche
            form.reach.data = current_user.influencer.reach
            form.profile_url.data = current_user.influencer.profile_url
            form.bio.data = current_user.influencer.bio

    return render_template('account/edit-profile.html', title='Account', form=form)


@login_required
@role_required(Role.SPONSOR)
@app.route("/sponsor-account", methods=['GET', 'POST'])
def sponsor_account_edit():
    form = SponsorRegistrationForm()
    if form.validate_on_submit():
        current_user.email = form.email.data
        sponsor = current_user.sponsor
        if sponsor is None:
            sponsor = Sponsor(
                user_id=current_user.id, 
                sponsor_name=form.sponsor_name.data, 
                website=form.website.data, 
                industry=form.industry.data, 
                market_valuation=form.market_valuation.data, 
                bio=form.bio.data
            )
            current_user.is_disabled = False
            db.session.add(sponsor)
        else:
            sponsor.sponsor_name = form.sponsor_name.data
            sponsor.website = form.website.data
            sponsor.industry = form.industry.data
            sponsor.market_valuation = form.market_valuation.data
            sponsor.bio = form.bio.data

        if form.picture.data:
            picture_file = save_picture(form.picture.data, folder_name="profile_pics")
            sponsor.image_file = picture_file

        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        if current_user.sponsor:
            form.sponsor_name.data = current_user.sponsor.sponsor_name
            form.industry.data = current_user.sponsor.industry
            form.market_valuation.data = current_user.sponsor.market_valuation
            form.website.data = current_user.sponsor.website
            form.bio.data = current_user.sponsor.bio

    return render_template('account/edit-profile-sponsor.html', title='Account', form=form)



@login_required
@role_required(Role.INFLUENCER, Role.SPONSOR)
@app.route("/account")
def account():
    if current_user.role == Role.SPONSOR.value:
        image_file = url_for('static', filename='profile_pics/' + current_user.sponsor.image_file)
        return render_template('profile/sponsor-profile.html', title='Profile', image_file=image_file)
    
    if current_user.role == Role.INFLUENCER.value:
        image_file = url_for('static', filename='profile_pics/' + current_user.influencer.image_file)
        return render_template('profile/influencer-profile.html', title='Profile', image_file=image_file)
    
    return "KUCH BHI MATCH NHI HUA"




@login_required
@role_required(Role.INFLUENCER, Role.SPONSOR)
@app.route("/profile/<id>")
def profile(id):
    user = User.query.get(id)
    print(user.role)
    if user and user.role == Role.SPONSOR.name:
        sponsor = Sponsor.query.get(user.sponsor.id)
        image_file = url_for('static', filename='profile_pics/' + sponsor.image_file)
        return render_template('visitors-account/sponsor.html', title='Profile', sponsor=sponsor,user=user, image_file=image_file)
    
    if user and user.role == Role.INFLUENCER.name:
        influencer = Influencer.query.get(user.influencer.id)
        image_file = url_for('static', filename='profile_pics/' + influencer.image_file)
        return render_template('visitors-account/influencer.html', title='Profile',influencer=influencer,user=user, image_file=image_file)







###########################################
################CAMPAIGN###################
###########################################

@login_required
@role_required(Role.SPONSOR)
@app.route("/create-campaign", methods=['GET', 'POST'])
def create_campaign():
    form = CampaignRegistrationForm()
    if form.validate_on_submit():
        campaign = Campaign(
            sponsor_id=current_user.sponsor.id,
            title=form.title.data,
            description=form.description.data,
            budget=form.budget.data,
            target_audience=form.target_audience.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            is_disabled=form.is_disabled.data
        )
        if form.picture.data:
            picture_file = save_picture(form.picture.data, folder_name="campaign_poster")
            campaign.image_file = picture_file

        db.session.add(campaign)
        db.session.commit()

        flash('Campaign has been created!', 'success')
        return redirect(url_for('home'))
    

    return render_template('create-campaign.html', title='About', form=form)





@login_required
@role_required(Role.SPONSOR)
@app.route("/edit-campaign/<campaign_id>", methods=['GET', 'POST'])
def edit_campaign(campaign_id):

    form = CampaignRegistrationForm()
    campaign = Campaign.query.filter_by(id=campaign_id).first()
    
    if campaign is None or campaign.sponsor_id != current_user.sponsor.id:
        flash("SOMETHING WENT WRONG!!!", "danger")
        return redirect(url_for('home'))

    if form.validate_on_submit():
        campaign.title=form.title.data
        campaign.description=form.description.data
        campaign.budget=form.budget.data
        campaign.target_audience=form.target_audience.data
        campaign.start_date=form.start_date.data
        campaign.end_date=form.end_date.data
        campaign.is_disabled=form.is_disabled.data
        
        if form.picture.data:
            picture_file = save_picture(form.picture.data, folder_name="campaign_poster/")
            campaign.image_file = picture_file

        db.session.add(campaign)
        db.session.commit()

        flash('Campaign has been updated!', 'success')
        return redirect(url_for('home'))
    else:
        form.title.data=campaign.title
        form.description.data=campaign.description
        form.budget.data=campaign.budget
        form.target_audience.data=campaign.target_audience
        form.start_date.data=campaign.start_date
        form.end_date.data=campaign.end_date
        form.is_disabled.data=campaign.is_disabled

    
    #Building requests
    campaign_reqs = []
    for req in campaign.influencer_requests:
        campaign_reqs.append({"influencer": Influencer.query.filter_by(id=req.influencer_id).first(), "request":req})

    #Contracts
    expenditure = 0
    deleted_contracts = []
    campaign_contracts = []
    for contract in campaign.influencer_contracts:
        expenditure += contract.budget
        if contract.is_deleted:
            deleted_contracts.append({"influencer": Influencer.query.filter_by(id=contract.influencer_id).first(), "contract":contract})
            continue
        campaign_contracts.append({"influencer": Influencer.query.filter_by(id=contract.influencer_id).first(), "contract":contract})
        
    return render_template('edit-campaign.html', title='About', form=form, campaign_reqs=campaign_reqs, campaign_contracts=campaign_contracts, expenditure=expenditure, deleted_contracts=deleted_contracts)



###################################################################333
##############################REST API####################################
#######################################################################



@login_required
@role_required(Role.INFLUENCER)
@app.route("/make-request/<campaign_id>/<influencer_id>", methods=['GET'])
def make_request(campaign_id, influencer_id):
    campaign = Campaign.query.filter_by(id=campaign_id).first()
    req = CampaignRequest.query.filter_by(campaign_id=campaign_id, influencer_id=influencer_id).first()
    if req is None and not campaign.is_disabled:
        req = CampaignRequest(campaign_id=campaign_id, influencer_id=influencer_id, budget=campaign.budget)
        db.session.add(req)
        db.session.commit()
    else:
        contract = Contract.query.filter_by(campaign_id=campaign_id, influencer_id=influencer_id, is_deleted=False).first()
        if contract is None:
            flash("Pending request", "warning")
        else:
            flash("Already Accepted", "success")
    ref = request.referrer
    return redirect(ref)




@login_required
@role_required(Role.SPONSOR)
@app.route("/delete-request/<campaign_id>/<influencer_id>", methods=['GET'])
def delete_request(campaign_id, influencer_id):
    req = CampaignRequest.query.filter_by(campaign_id=campaign_id, influencer_id=influencer_id).first()
    if req is not None:
        db.session.delete(req)
        db.session.commit()

    ref = request.referrer
    return redirect(ref)




@login_required
@role_required(Role.SPONSOR)
@app.route("/make-contract/<campaign_id>/<campaign_request_id>", methods=['GET'])
def make_contract(campaign_id, campaign_request_id):
 
    campaign = Campaign.query.get(campaign_id)
    campaign_request = CampaignRequest.query.get(campaign_request_id)
    influencer = Influencer.query.get(campaign_request.influencer_id)
    contract = Contract.query.filter_by(campaign_id=campaign_id, influencer_id=influencer.id, is_deleted=False).first()

    if contract is None and not campaign.is_disabled:
        contract = Contract(campaign_id=campaign_id,sponsor_id=campaign.sponsor_id, influencer_id=influencer.id, reach=influencer.reach, budget=campaign.budget)
        db.session.add(contract)
        db.session.delete(campaign_request)
        db.session.commit()
    else:
        flash("Campaign is already subscribed by!", "warning")

    ref = request.referrer
    return redirect(ref)



@login_required
@role_required(Role.SPONSOR)
@app.route("/delete-contract/<campaign_id>/<influencer_id>", methods=['GET'])
def delete_contract(campaign_id, influencer_id):
    contract = Contract.query.filter_by(campaign_id=campaign_id, influencer_id=influencer_id, is_deleted=False).first()
    
    if contract is not None:
        contract.is_deleted = True
        contract.deleted_at = datetime.now()
        db.session.commit()
    
    ref = request.referrer
    return redirect(ref)



@login_required
@role_required(Role.INFLUENCER)
@app.route("/my-campaigns")
def my_contracts():
    contracts = (
        Contract.query
            .filter_by(
                influencer_id = current_user.influencer.id
                )
            .join(Campaign, Campaign.id==Contract.campaign_id)
            .add_columns(Campaign.description,
                         Campaign.start_date,
                         Campaign.end_date,
                         Campaign.title,
                         Contract.budget)
            .all())
    
    reqs = (
        CampaignRequest.query
            .filter_by(
                influencer_id = current_user.influencer.id
                )
            .join(Campaign, Campaign.id==CampaignRequest.campaign_id)
            .add_columns(Campaign.description,
                         Campaign.start_date,
                         Campaign.end_date,
                         Campaign.title,
                         CampaignRequest.influencer_id,
                         CampaignRequest.campaign_id,
                         Campaign.budget)
            .all())
    
    return render_template('my-contracts.html', contracts=contracts, reqs=reqs)
