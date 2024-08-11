from flask import render_template
from sqlalchemy import func
from base import app, db
from base.models import Campaign, Sponsor
from base.forms import CATEGORY_CHOICES

@app.route("/stats")
def stats():
    # Extract categories
    category = [internal_value for internal_value, _ in CATEGORY_CHOICES[1:]]
    
    # Initialize data containers
    category_data = []
    
    # Join Campaign and Sponsor and add the Sponsor.industry column
    data = Campaign.query.join(Sponsor, Campaign.sponsor_id == Sponsor.id).add_columns(Sponsor.industry)

    # Collect campaign count and budget sum for each category
    for cat in category:
        campaigns_count = data.filter(Sponsor.industry == cat).count()
        budgets_sum = data.filter(Sponsor.industry == cat).with_entities(func.sum(Campaign.budget)).scalar() or 0
        
        category_data.append({
            'category': cat,
            'campaigns': campaigns_count,
            'total_budget': budgets_sum
        })

    # Extract data for chart
    names = [entry['category'] for entry in category_data]
    counts = [entry['campaigns'] for entry in category_data]
    budgets_sum = [entry['total_budget'] for entry in category_data]

    return render_template("stats.html", names=names, counts=counts, budgets_sum=budgets_sum)
