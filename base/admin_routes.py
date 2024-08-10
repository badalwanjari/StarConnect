from flask import redirect, render_template, request
from sqlalchemy import func
from base import app, db
from base.models import Campaign, Influencer, Sponsor, User

@app.route("/admin")
def admin_home():

    sponsors = (
            Sponsor.query
            .join(User, Sponsor.user_id == User.id)
            .outerjoin(Sponsor.sponsor_campaigns)
            .outerjoin(Sponsor.sponsor_campaigns)
            .add_columns(
                User.is_banned,
                User.email,
                Sponsor.sponsor_name,
                Sponsor.industry,
                Sponsor.market_valuation,
                Sponsor.user_id,
                func.count(Sponsor.sponsor_campaigns).label("contract_count"),
                func.count(Sponsor.sponsor_campaigns).label("campaign_count")
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
    
    print(campaigns)


    return render_template('admin-pages/home.html', 
                           sponsors=sponsors, \
                           influencers=influencers, \
                           campaigns=campaigns,
                          )


@app.route("/admin/flag/campaign/<id>")
def flag_campaign(id):
    campaign = Campaign.query.get(id)
    campaign.is_flagged = not campaign.is_flagged
    db.session.commit()
    return redirect(request.referrer)



@app.route("/admin/ban/user/<id>")
def ban_user(id):
    user = User.query.get(id)
    user.is_banned = not user.is_banned
    db.session.commit()

    return redirect(request.referrer)


