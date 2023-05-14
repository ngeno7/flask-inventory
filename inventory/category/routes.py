from flask import Blueprint, render_template

categories = Blueprint('categories', __name__, url_prefix='/categories')

@categories.route('')
def index():
    
    return render_template("category/index.html", title="Categories")