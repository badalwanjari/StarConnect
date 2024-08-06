from datetime import datetime
from base import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    sponsor = db.relationship('Sponsor', backref='sponsor', uselist=False)
    influencer = db.relationship('Influencer', backref='influencer', uselist=False)
    is_disabled = db.Column(db.Boolean, default=True)
    role = db.Column(db.String(), default="INFLUENCER")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    


class Sponsor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    sponsor_name = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100))
    market_valuation = db.Column(db.Integer())
    bio = db.Column(db.Text(), nullable=True)
    website = db.Column(db.String(50), default="-")
    image_file = db.Column(db.String(50), nullable=False, default='default-sponsor.jpg')
    complaigns = db.relationship('Campaign', backref='campaigns', uselist=True)

    def __repr__(self) -> str:
        return f"Sponser('{self.sponsor_name}', '{self.industry}')"
    



class Influencer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    influencer_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    niche = db.Column(db.String(100), nullable=False)
    reach = db.Column(db.Integer, nullable=False)
    profile_url = db.Column(db.String(100), nullable=True)
    image_file = db.Column(db.String(50), nullable=False, default='default.jpg')
    bio = db.Column(db.Text(), nullable=True)
    CampaignRequests = db.relationship('CampaignRequest', backref='CampaignRequests', uselist=True)
    campaign_contracts = db.relationship('Contract', backref='campaign_contracts', uselist=True)

    def __repr__(self):
        return f"Influencer('{self.influencer_name}', '{self.category}')"



class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsor.id'))
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    target_audience = db.Column(db.String(20))
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    image_file = db.Column(db.String(50), nullable=False, default='default.jpg')
    is_disabled = db.Column(db.Boolean, default=True)
    is_deleted = db.Column(db.Boolean, default=False)
    is_flagged = db.Column(db.Boolean, default=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())
    influencer_requests = db.relationship('CampaignRequest', backref='influencer_requests', uselist=True)
    influencer_contracts = db.relationship('Contract', backref='influencer_contracts', uselist=True)

    def __repr__(self):
        return f"Campaign('{self.title}', '{self.budget}')"
    


class CampaignRequest(db.Model):
    __tablename__ = 'campaign_request'
 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Ensure id is auto-increment
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencer.id'), nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)


class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencer.id'))
    budget = db.Column(db.Integer)
    reach = db.Column(db.Integer)
    # deletedby_influencer = db.Column(db.Boolean, default=False)
    # deletedby_sponsor = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    