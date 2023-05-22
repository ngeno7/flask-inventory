from flask import Blueprint, render_template, request
from flask_login import login_required
from .form import CategoryForm
from .models import Category
categories = Blueprint('categories', __name__, url_prefix='/categories')
from ..db import db

@categories.route('', methods=['GET', 'POST'])
@login_required
def index():
    form = CategoryForm()
    category = Category()
    if request.form.get('id'):
        category = Category.query.filter_by(id=request.form.get('id')).first()
    if request.method == 'POST' and form.validate_on_submit():
        category.name = form.name.data
        category.description = form.description.data
        category.active = True
        db.session.add(category)
        db.session.commit()

    categories = Category.query.all()
    return render_template("category/index.html", title="Categories", categories=categories, form=form)
