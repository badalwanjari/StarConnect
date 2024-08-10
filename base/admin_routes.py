from flask import redirect, render_template, request
from base import app, db
from base.models import Campaign, Influencer, Sponsor

@app.route("/admin")
def admin_home():
    sponsors = Sponsor.query.all()
    influencers = Influencer.query.all()
    campaigns = Campaign.query.join(Sponsor, Campaign.sponsor_id==Sponsor.id).add_columns(Campaign.id, Campaign.title, Campaign.date_posted, Campaign.budget, Campaign.is_flagged, Sponsor.sponsor_name).all()

    expenditure = 0
    for campaign in campaigns:
        expenditure += campaign.budget
    
    campaigns.reverse()
    return render_template('admin-pages/home.html', 
                           sponsors=sponsors, \
                           influencers=influencers, \
                           campaigns=campaigns,
                           expenditure=expenditure)


@app.route("/admin/flag/campaign/<id>")
def flag_campaign(id):
    campaign = Campaign.query.get(id)
    campaign.is_flagged = not campaign.is_flagged
    db.session.commit()
    return redirect(request.referrer)

