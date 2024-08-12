from base.models import User, Sponsor, Influencer
from datetime import datetime

def create_db(app, db): 

    with app.app_context():
        db.drop_all()
        db.create_all()
        admin = User(id=1, username="admin", email="admin@gmail.com", password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role="ADMIN", is_disabled=False)
        db.session.add(admin)
        db.session.commit()
        


def add_data(app, db):

    with app.app_context():
        pass
        
        
