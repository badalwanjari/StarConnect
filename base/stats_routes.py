from flask import render_template
from flask_login import current_user
from sqlalchemy import func
from base import app, db
from base.models import Campaign, Contract, Sponsor
from base.forms import CATEGORY_CHOICES
from base.routes import Role

@app.route("/stats")
def stats():
    category = [internal_value for internal_value, _ in CATEGORY_CHOICES[1:]]
    
    category_data = []
    data = None

    
    if current_user.role == Role.INFLUENCER.value:
        data = (
            Contract.query
                .filter_by(influencer_id=current_user.influencer.id)
                .join(Campaign, Contract.campaign_id==Campaign.id)
                .add_column(Campaign.category)
                .all()
            )
    elif current_user.role == Role.SPONSOR.value:
        data = (
            Contract.query
                .filter_by(sponsor_id=current_user.sponsor.id)
                .join(Campaign, Contract.campaign_id==Campaign.id)
                .add_column(Campaign.category)
                .all()
            )
    else:
        data = (
            Contract.query
                .join(Campaign, Contract.campaign_id==Campaign.id)
                .add_column(Campaign.category)
                .all()
            )
    
    total = 0
    n = 0
    for cat_ in category:
        campaigns_count = 0
        budgets_sum = 0
        
        for contract, cat in data:
            if cat == cat_:
                campaigns_count += 1
                budgets_sum += contract.budget

        total += budgets_sum
        n += campaigns_count
        category_data.append({
            'category': cat_,
            'campaigns': campaigns_count,
            'total_budget': budgets_sum
        })

    additional = {
        "total": total,
        "average": total / n if n != 0 else 0, 
        "n": n
    }

    # Extract data for chart
    names = [entry['category'] for entry in category_data]
    counts = [entry['campaigns'] for entry in category_data]
    budgets_sum = [entry['total_budget'] for entry in category_data]

    return render_template("stats.html", additional=additional, names=names, counts=counts, budgets_sum=budgets_sum)
