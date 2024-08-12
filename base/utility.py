from .models import Campaign, Contract, Influencer, Sponsor, User

from datetime import datetime

def add_dummy_data(app, db):
    
    with app.app_context():

        users = [
            User(username='sponsor1', email='sponsor1@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor2', email='sponsor2@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor3', email='sponsor3@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor4', email='sponsor4@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor5', email='sponsor5@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor6', email='sponsor6@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor7', email='sponsor7@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor8', email='sponsor8@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor9', email='sponsor9@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor10', email='sponsor10@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor11', email='sponsor11@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor12', email='sponsor12@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor13', email='sponsor13@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor14', email='sponsor14@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor15', email='sponsor15@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor16', email='sponsor16@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor17', email='sponsor17@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor18', email='sponsor18@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor19', email='sponsor19@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False),
            User(username='sponsor20', email='sponsor20@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='SPONSOR', is_disabled=False)
        ]

        db.session.bulk_save_objects(users)
        db.session.commit()

        users = [
            User(username='influencer1', email='influencer1@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer2', email='influencer2@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer3', email='influencer3@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer4', email='influencer4@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer5', email='influencer5@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer6', email='influencer6@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer7', email='influencer7@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer8', email='influencer8@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer9', email='influencer9@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer10', email='influencer10@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer11', email='influencer11@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer12', email='influencer12@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer13', email='influencer13@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer14', email='influencer14@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer15', email='influencer15@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer16', email='influencer16@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer17', email='influencer17@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer18', email='influencer18@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer19', email='influencer19@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer20', email='influencer20@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer21', email='influencer21@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer22', email='influencer22@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer23', email='influencer23@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer24', email='influencer24@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer25', email='influencer25@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer26', email='influencer26@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer27', email='influencer27@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer28', email='influencer28@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer29', email='influencer29@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer30', email='influencer30@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer31', email='influencer31@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer32', email='influencer32@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer33', email='influencer33@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer34', email='influencer34@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer35', email='influencer35@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer36', email='influencer36@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer37', email='influencer37@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer38', email='influencer38@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer39', email='influencer39@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer40', email='influencer40@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer41', email='influencer41@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer42', email='influencer42@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer43', email='influencer43@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer44', email='influencer44@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer45', email='influencer45@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer46', email='influencer46@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer47', email='influencer47@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer48', email='influencer48@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer49', email='influencer49@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False),
            User(username='influencer50', email='influencer50@example.com', password="$2a$12$Sq71nH6GwpwRWpfKwFMR4e9owaKLhAUER5CeSTGJlYf4ued.aovja", role='INFLUENCER', is_disabled=False)
        ]

        db.session.bulk_save_objects(users)
        db.session.commit()


        
        sponsors = [
            Sponsor(user_id=1, sponsor_name='Fashionista Inc.', industry='fashion', market_valuation=15000000, bio='Leading fashion brand in the industry.', website='http://fashionista.com'),
            Sponsor(user_id=2, sponsor_name='Beauty Bloom', industry='beauty', market_valuation=8000000, bio='Innovative beauty products for modern women.', website='http://beautybloom.com'),
            Sponsor(user_id=3, sponsor_name='Globetrotter Adventures', industry='travel', market_valuation=12000000, bio='Top travel agency for exotic destinations.', website='http://globetrotter.com'),
            Sponsor(user_id=4, sponsor_name='Foodies Heaven', industry='food', market_valuation=5000000, bio='Culinary delights for the food lover in you.', website='http://foodiesheaven.com'),
            Sponsor(user_id=5, sponsor_name='FitLife Co.', industry='fitness', market_valuation=7000000, bio='Your partner in achieving fitness goals.', website='http://fitlife.com'),
            Sponsor(user_id=6, sponsor_name='TechWorld Solutions', industry='tech', market_valuation=20000000, bio='Pioneering tech innovations for the future.', website='http://techworld.com'),
            Sponsor(user_id=7, sponsor_name='Urban Style', industry='fashion', market_valuation=10000000, bio='Urban fashion trends for the modern generation.', website='http://urbanstyle.com'),
            Sponsor(user_id=8, sponsor_name='GlowUp Cosmetics', industry='beauty', market_valuation=9000000, bio='Affordable beauty products with luxury quality.', website='http://glowup.com'),
            Sponsor(user_id=9, sponsor_name='Voyage Ventures', industry='travel', market_valuation=15000000, bio='Exclusive travel experiences for adventurers.', website='http://voyageventures.com'),
            Sponsor(user_id=10, sponsor_name='Gourmet Delight', industry='food', market_valuation=6000000, bio='High-end gourmet food for the discerning palate.', website='http://gourmetdelight.com'),
            Sponsor(user_id=11, sponsor_name='ActiveFit', industry='fitness', market_valuation=9000000, bio='Active wear and fitness accessories.', website='http://activefit.com'),
            Sponsor(user_id=12, sponsor_name='NextGen Tech', industry='tech', market_valuation=18000000, bio='Tech solutions for the next generation.', website='http://nextgen.com'),
            Sponsor(user_id=13, sponsor_name='Chic Couture', industry='fashion', market_valuation=7000000, bio='Luxury fashion brand with a modern twist.', website='http://chiccouture.com'),
            Sponsor(user_id=14, sponsor_name='Radiant Beauty', industry='beauty', market_valuation=11000000, bio='Radiating beauty from within.', website='http://radiantbeauty.com'),
            Sponsor(user_id=15, sponsor_name='Nomad Escapes', industry='travel', market_valuation=14000000, bio='Escape the ordinary with our unique travel experiences.', website='http://nomadescapes.com'),
            Sponsor(user_id=16, sponsor_name='The Culinary Corner', industry='food', market_valuation=6500000, bio='Culinary experiences that tantalize the senses.', website='http://culinarycorner.com'),
            Sponsor(user_id=17, sponsor_name='FitFlex', industry='fitness', market_valuation=9500000, bio='Flexible fitness programs for every lifestyle.', website='http://fitflex.com'),
            Sponsor(user_id=18, sponsor_name='Digital Innovators', industry='tech', market_valuation=17000000, bio='Innovative digital solutions for businesses.', website='http://digitalinnovators.com'),
            Sponsor(user_id=19, sponsor_name='Vogue Style', industry='fashion', market_valuation=8500000, bio='Vogue-worthy fashion for everyday wear.', website='http://voguestyle.com'),
            Sponsor(user_id=20, sponsor_name='Luxe Beauty', industry='beauty', market_valuation=10000000, bio='Luxurious beauty products for the modern woman.', website='http://luxebeauty.com')
        ]

        db.session.bulk_save_objects(sponsors)
        db.session.commit()

        influencers = [
            Influencer(user_id=21, influencer_name='Ava Johnson', category='fashion', niche='Streetwear', reach=50000, profile_url='http://instagram.com/avajohnson', image_file='ava.jpg', bio='Fashion influencer with a love for streetwear.'),
            Influencer(user_id=22, influencer_name='Mia Thompson', category='Beauty', niche='Skincare', reach=120000, profile_url='http://instagram.com/miathompson', image_file='mia.jpg', bio='Beauty enthusiast sharing skincare tips and tricks.'),
            Influencer(user_id=23, influencer_name='Liam Brown', category='travel', niche='Adventure', reach=80000, profile_url='http://instagram.com/liambrown', image_file='liam.jpg', bio='Adventure traveler exploring the wild.'),
            Influencer(user_id=24, influencer_name='Olivia Davis', category='food', niche='Vegan', reach=60000, profile_url='http://instagram.com/oliviadavis', image_file='olivia.jpg', bio='Vegan food blogger and recipe developer.'),
            Influencer(user_id=25, influencer_name='Noah Wilson', category='fitness', niche='Bodybuilding', reach=70000, profile_url='http://instagram.com/noahwilson', image_file='noah.jpg', bio='Bodybuilder sharing workout routines and diet tips.'),
            Influencer(user_id=26, influencer_name='Sophia Martinez', category='tech', niche='Gadgets', reach=90000, profile_url='http://instagram.com/sophiamartinez', image_file='sophia.jpg', bio='Tech reviewer focusing on the latest gadgets.'),
            Influencer(user_id=27, influencer_name='Ella Smith', category='fashion', niche='Sustainable Fashion', reach=75000, profile_url='http://instagram.com/ellasmith', image_file='ella.jpg', bio='Promoting sustainable fashion choices.'),
            Influencer(user_id=28, influencer_name='Isabella Garcia', category='Beauty', niche='Makeup', reach=110000, profile_url='http://instagram.com/isabellagarcia', image_file='isabella.jpg', bio='Makeup artist sharing tutorials and tips.'),
            Influencer(user_id=29, influencer_name='Ethan Miller', category='travel', niche='Luxury Travel', reach=95000, profile_url='http://instagram.com/ethanmiller', image_file='ethan.jpg', bio='Luxury travel blogger showcasing the finest experiences.'),
            Influencer(user_id=30, influencer_name='Emily Anderson', category='food', niche='Desserts', reach=65000, profile_url='http://instagram.com/emilyanderson', image_file='emily.jpg', bio='Dessert lover sharing sweet recipes.'),
            Influencer(user_id=31, influencer_name='Lucas Scott', category='fitness', niche='CrossFit', reach=85000, profile_url='http://instagram.com/lucasscott', image_file='lucas.jpg', bio='CrossFit athlete sharing workouts and motivation.'),
            Influencer(user_id=32, influencer_name='Grace Lee', category='tech', niche='Software', reach=100000, profile_url='http://instagram.com/gracelee', image_file='grace.jpg', bio='Software engineer reviewing the latest in tech.'),
            Influencer(user_id=33, influencer_name='Harper Adams', category='fashion', niche='High Fashion', reach=130000, profile_url='http://instagram.com/harperadams', image_file='harper.jpg', bio='High fashion influencer with a passion for luxury.'),
            Influencer(user_id=34, influencer_name='Henry Walker', category='Beauty', niche='Men’s Grooming', reach=50000, profile_url='http://instagram.com/henrywalker', image_file='henry.jpg', bio='Men’s grooming expert sharing tips for the modern man.'),
            Influencer(user_id=35, influencer_name='Avery Thomas', category='travel', niche='Backpacking', reach=60000, profile_url='http://instagram.com/averythomas', image_file='avery.jpg', bio='Backpacking across the globe, one adventure at a time.'),
            Influencer(user_id=36, influencer_name='Charlotte White', category='food', niche='Healthy Eating', reach=70000, profile_url='http://instagram.com/charlottewhite', image_file='charlotte.jpg', bio='Sharing healthy recipes and nutrition tips.'),
            Influencer(user_id=37, influencer_name='Daniel Harris', category='fitness', niche='Yoga', reach=90000, profile_url='http://instagram.com/danielharris', image_file='daniel.jpg', bio='Yoga instructor spreading mindfulness and wellness.'),
            Influencer(user_id=38, influencer_name='Zoey Martinez', category='tech', niche='AI & Robotics', reach=110000, profile_url='http://instagram.com/zoeymartinez', image_file='zoey.jpg', bio='Exploring the latest in AI and robotics.'),
            Influencer(user_id=39, influencer_name='Hannah Clark', category='fashion', niche='Vintage Fashion', reach=85000, profile_url='http://instagram.com/hannahclark', image_file='hannah.jpg', bio='Vintage fashion lover with a passion for retro styles.'),
            Influencer(user_id=40, influencer_name='Michael Wright', category='Beauty', niche='Fragrance', reach=60000, profile_url='http://instagram.com/michaelwright', image_file='michael.jpg', bio='Fragrance enthusiast exploring scents from around the world.'),
            Influencer(user_id=41, influencer_name='Amelia King', category='travel', niche='Cultural Travel', reach=70000, profile_url='http://instagram.com/ameliaking', image_file='amelia.jpg', bio='Cultural travel experiences from every corner of the globe.'),
            Influencer(user_id=42, influencer_name='James Green', category='food', niche='BBQ', reach=90000, profile_url='http://instagram.com/jamesgreen', image_file='james.jpg', bio='BBQ master sharing tips and recipes for grilling.'),
            Influencer(user_id=43, influencer_name='Lily Lewis', category='fitness', niche='Pilates', reach=100000, profile_url='http://instagram.com/lilylewis', image_file='lily.jpg', bio='Pilates instructor helping you strengthen and tone.'),
            Influencer(user_id=44, influencer_name='Sebastian Young', category='tech', niche='Gaming', reach=150000, profile_url='http://instagram.com/sebastianyoung', image_file='sebastian.jpg', bio='Gaming expert reviewing the latest titles and gear.'),
            Influencer(user_id=45, influencer_name='Victoria Adams', category='fashion', niche='Casual Wear', reach=75000, profile_url='http://instagram.com/victoriaadams', image_file='victoria.jpg', bio='Casual wear influencer promoting comfort and style.'),
            Influencer(user_id=46, influencer_name='Jack Hill', category='Beauty', niche='Haircare', reach=120000, profile_url='http://instagram.com/jackhill', image_file='jack.jpg', bio='Haircare specialist sharing tips for every hair type.'),
            Influencer(user_id=47, influencer_name='Scarlett Baker', category='travel', niche='Ecotourism', reach=85000, profile_url='http://instagram.com/scarlettbaker', image_file='scarlett.jpg', bio='Ecotourism advocate exploring sustainable travel.'),
            Influencer(user_id=48, influencer_name='Zachary Roberts', category='food', niche='Baking', reach=95000, profile_url='http://instagram.com/zacharyroberts', image_file='zachary.jpg', bio='Baking expert sharing delicious recipes and tips.'),
            Influencer(user_id=49, influencer_name='Ella King', category='fitness', niche='Running', reach=70000, profile_url='http://instagram.com/ellaking', image_file='ella_king.jpg', bio='Runner sharing training tips and marathon experiences.'),
            Influencer(user_id=50, influencer_name='Daniel Phillips', category='tech', niche='Startups', reach=120000, profile_url='http://instagram.com/danielphillips', image_file='danielp.jpg', bio='Startup enthusiast and tech entrepreneur.'),
            Influencer(user_id=51, influencer_name='Avery Wilson', category='fashion', niche='Swimwear', reach=60000, profile_url='http://instagram.com/averywilson', image_file='averyw.jpg', bio='Swimwear fashion influencer.'),
            Influencer(user_id=52, influencer_name='Mason Hernandez', category='Beauty', niche='Skincare for Men', reach=50000, profile_url='http://instagram.com/masonhernandez', image_file='masonh.jpg', bio='Promoting skincare for men.'),
            Influencer(user_id=53, influencer_name='Zoe Moore', category='travel', niche='Solo Travel', reach=85000, profile_url='http://instagram.com/zoemoore', image_file='zoem.jpg', bio='Solo traveler sharing tips and stories.'),
            Influencer(user_id=54, influencer_name='Aria Peterson', category='food', niche='Plant-Based', reach=95000, profile_url='http://instagram.com/ariapeterson', image_file='ariap.jpg', bio='Plant-based recipe creator and food lover.'),
            Influencer(user_id=55, influencer_name='Benjamin Lee', category='fitness', niche='Strength Training', reach=110000, profile_url='http://instagram.com/benjaminlee', image_file='benjaminl.jpg', bio='Strength training and powerlifting expert.'),
            Influencer(user_id=56, influencer_name='Elizabeth Walker', category='tech', niche='AI & ML', reach=130000, profile_url='http://instagram.com/elizabethwalker', image_file='elizabethw.jpg', bio='AI and Machine Learning enthusiast.'),
            Influencer(user_id=57, influencer_name='Jackson Carter', category='fashion', niche='Athleisure', reach=90000, profile_url='http://instagram.com/jacksoncarter', image_file='jacksonc.jpg', bio='Athleisure fashion influencer.'),
            Influencer(user_id=58, influencer_name='Luna Cooper', category='Beauty', niche='Organic Beauty', reach=60000, profile_url='http://instagram.com/lunacooper', image_file='lunac.jpg', bio='Organic beauty product reviewer.'),
            Influencer(user_id=59, influencer_name='Ella Parker', category='travel', niche='Family Travel', reach=120000, profile_url='http://instagram.com/ellaparker', image_file='ellap.jpg', bio='Family travel blogger sharing experiences.'),
            Influencer(user_id=60, influencer_name='Jacob Morgan', category='food', niche='Culinary Arts', reach=140000, profile_url='http://instagram.com/jacobmorgan', image_file='jacobm.jpg', bio='Culinary arts expert and food lover.')
        ]

        db.session.bulk_save_objects(influencers)
        db.session.commit()

        campaigns = [
            Campaign(sponsor_id=1, title='Streetwear Spring Collection', description='Promoting our latest streetwear collection for the spring season.', budget=200000, target_audience='Youth', category='fashion', start_date=datetime(2024, 9, 1), end_date=datetime(2024, 9, 30), is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=2, title='Summer Skincare Launch', description='Introducing our new summer skincare line for glowing skin.', budget=150000, target_audience='Women', category='Beauty', start_date=datetime(2024, 8, 15), end_date=datetime(2024, 9, 15),  is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=3, title='Adventure Travel Contest', description='Join our adventure travel contest and win exciting prizes.', budget=100000, target_audience='Adults', category='travel', start_date=datetime(2024, 8, 10), end_date=datetime(2024, 8, 31),  is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=4, title='Gourmet Cooking Classes', description='Sign up for our exclusive gourmet cooking classes.', budget=50000, target_audience='Food Enthusiasts', category='food', start_date=datetime(2024, 8, 20), end_date=datetime(2024, 9, 20),  is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=5, title='Fitness Challenge', description='Participate in our fitness challenge and get in shape.', budget=75000, target_audience='Fitness Enthusiasts', category='fitness', start_date=datetime(2024, 8, 1), end_date=datetime(2024, 8, 31),  is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=6, title='Tech Gadget Giveaway', description='Enter our tech gadget giveaway for a chance to win the latest devices.', budget=120000, target_audience='Tech Enthusiasts', category='tech', start_date=datetime(2024, 8, 5), end_date=datetime(2024, 8, 20), is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=7, title='Urban Fashion Week', description='Join us for Urban Fashion Week and discover the latest trends.', budget=300000, target_audience='Fashion Lovers', category='fashion', start_date=datetime(2024, 9, 10), end_date=datetime(2024, 9, 17),  is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=8, title='Luxury Makeup Line Launch', description='Experience the launch of our new luxury makeup line.', budget=180000, target_audience='Women', category='Beauty', start_date=datetime(2024, 8, 25), end_date=datetime(2024, 9, 5), is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=9, title='Exclusive Travel Packages', description='Book our exclusive travel packages for your next adventure.', budget=220000, target_audience='Travel Enthusiasts', category='travel', start_date=datetime(2024, 8, 15), end_date=datetime(2024, 8, 31), is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=10, title='Gourmet Tasting Event', description='Join our gourmet tasting event and indulge in culinary delights.', budget=50000, target_audience='Foodies', category='food', start_date=datetime(2024, 9, 5), end_date=datetime(2024, 9, 10), is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=11, title='ActiveFit Gear Promotion', description='Get discounts on ActiveFit gear this season.', budget=80000, target_audience='Fitness Enthusiasts', category='fitness', start_date=datetime(2024, 8, 10), end_date=datetime(2024, 8, 20), is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=12, title='Future Tech Expo', description='Attend our Future Tech Expo and explore the latest innovations.', budget=250000, target_audience='Tech Innovators', category='tech', start_date=datetime(2024, 8, 15), end_date=datetime(2024, 8, 30), is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=13, title='Luxury Fashion Showcase', description='Discover luxury fashion at our exclusive showcase event.', budget=400000, target_audience='Fashion Enthusiasts', category='fashion', start_date=datetime(2024, 9, 12), end_date=datetime(2024, 9, 18),  is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=14, title='Radiant Beauty Awards', description='Vote for your favorite beauty products in our Radiant Beauty Awards.', budget=60000, target_audience='Beauty Lovers', category='Beauty', start_date=datetime(2024, 8, 25), end_date=datetime(2024, 9, 10),  is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=15, title='Nomad Travel Festival', description='Experience the Nomad Travel Festival with exclusive deals and workshops.', budget=300000, target_audience='Travel Enthusiasts', category='travel', start_date=datetime(2024, 9, 10), end_date=datetime(2024, 9, 20),  is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=16, title='Culinary Arts Fair', description='Attend the Culinary Arts Fair and explore diverse cuisines.', budget=70000, target_audience='Food Enthusiasts', category='food', start_date=datetime(2024, 8, 22), end_date=datetime(2024, 8, 25),  is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=17, title='FitFlex Yoga Retreat', description='Join us for the FitFlex Yoga Retreat and rejuvenate your mind and body.', budget=120000, target_audience='Fitness Enthusiasts', category='fitness', start_date=datetime(2024, 9, 5), end_date=datetime(2024, 9, 10),  is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=18, title='Digital Innovators Summit', description='Attend the Digital Innovators Summit and learn from industry leaders.', budget=280000, target_audience='Tech Entrepreneurs', category='tech', start_date=datetime(2024, 9, 1), end_date=datetime(2024, 9, 3),  is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=19, title='Vogue Style Fashion Show', description='Watch the latest fashion trends at the Vogue Style Fashion Show.', budget=350000, target_audience='Fashion Enthusiasts', category='fashion', start_date=datetime(2024, 9, 8), end_date=datetime(2024, 9, 12), is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now()),
            Campaign(sponsor_id=20, title='Luxe Beauty Conference', description='Attend the Luxe Beauty Conference to learn from top beauty experts.', budget=90000, target_audience='Beauty Professionals', category='Beauty', start_date=datetime(2024, 9, 15), end_date=datetime(2024, 9, 17), is_disabled=False, is_deleted=False, is_flagged=False, date_posted=datetime.now())
        ]

        db.session.bulk_save_objects(campaigns)
        db.session.commit()

