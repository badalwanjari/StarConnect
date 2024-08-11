from base.models import User, Sponsor, Influencer
from datetime import datetime

def create_db(app, db): 

    with app.app_context():
        db.drop_all()
        db.create_all()
        


def add_data(app, db):

    with app.app_context():

        user = User(id=1, username="admin", email="admin@gmail.com", password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role="ADMIN", is_disabled=False)

        # user1 = User(id=1, username="badal", email="b@gmail.com", password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role="INFLUENCER", is_disabled=False)
        # user2 = User(id=2, username="persistent", email="p@gmail.com", password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role="SPONSOR", is_disabled=False)

        # influencer = Influencer(user_id=1, influencer_name="Badal Wanjari", category="travel", niche="Men", reach="12000",profile_url="insta.com/badalwanjari", bio="Hello this badal wanjari")
        # sponsor = Sponsor(user_id=2, sponsor_name="PSL", industry="travel", market_valuation=100000, bio="THis is travel agency", website="psl.org")
        
        # db.session.add(user1)
        # db.session.add(user2)
        # db.session.add(influencer)
        # db.session.add(sponsor)
        
        db.session.add(user)

        db.session.commit()
