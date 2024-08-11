from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from sqlalchemy import func
from base import app, db, bcrypt
from base.forms import LoginForm
from base.models import Campaign, Influencer, Sponsor, User
from base.routes import Role, role_required

@app.route("/admin")
@role_required(Role.ADMIN.value)
def admin_home():
    sponsors = (
        Sponsor.query
        .join(User, Sponsor.user_id == User.id)
        .outerjoin(Sponsor.sponsor_campaigns)
        .add_columns(
            User.is_banned,
            User.email,
            Sponsor.sponsor_name,
            Sponsor.industry,
            Sponsor.market_valuation,
            Sponsor.user_id,
            func.count().filter(Sponsor.sponsor_campaigns).label("campaign_count")
        )
        .group_by(
            Sponsor.id,
        )
        .all()
    )
        
    influencers = (
            Influencer.query
            .join(User, Influencer.user_id == User.id)
            .outerjoin(Influencer.campaign_contracts)  # Ensure this matches the relationship name
            .add_columns(
                Influencer.user_id,
                Influencer.influencer_name,
                User.is_banned,
                User.email,
                Influencer.reach,
                func.count(Influencer.campaign_contracts).label("contract_count"),
                Influencer.category
            )
            .group_by(
                Influencer.user_id
            )
            .all()
        )
    

    campaigns = (
        Campaign.query
        .join(Sponsor, Campaign.sponsor_id == Sponsor.id)
        .outerjoin(Campaign.influencer_contracts)
        .add_columns(
            Campaign.id, 
            Campaign.title, 
            Campaign.date_posted, 
            Campaign.budget, 
            Campaign.is_flagged, 
            Sponsor.sponsor_name,
            func.count(Campaign.influencer_contracts).label("influencer_count"),
            func.sum(Campaign.budget).label("expenditure")
        )
        .group_by(
            Campaign.id
        )
        .all()
    )
    
    return render_template('admin-pages/home.html', 
                           sponsors=sponsors, \
                           influencers=influencers, \
                           campaigns=campaigns,
                          )




@role_required(Role.ADMIN.value)
@app.route("/admin/flag/campaign/<id>")
def flag_campaign(id):
    campaign = Campaign.query.get(id)
    campaign.is_flagged = not campaign.is_flagged
    db.session.commit()
    return redirect(request.referrer)



@role_required(Role.ADMIN.value)
@app.route("/admin/ban/user/<id>")
def ban_user(id):
    user = User.query.get(id)
    user.is_banned = not user.is_banned
    db.session.commit()
    return redirect(request.referrer)




@app.route("/admin/login", methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data, role=Role.ADMIN.value).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin_home'))
        else:
            flash('Admin Login Unsuccessful. Please check email and password', 'danger')

    return render_template('admin-pages/admin-login.html', title='Login', form=form)
