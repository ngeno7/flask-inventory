from flask import Blueprint, render_template, url_for, redirect, flash
from ..category.models import Category

inventory = Blueprint('inventory', __name__, url_prefix='/inventory')

@inventory.route('', methods=['GET'])
def index():

    return render_template("inventory/index.html", title="Inventory")

@inventory.route('/form', methods=['GET', 'POST'])
def form():
    categories = Category.query.filter_by(active=True).all()
    return render_template("inventory/form.html", title='Inventory', categories=categories)

@inventory.route('/form/<id>', methods=['GET', 'POST'])
def edit(id):

    categories = Category.query.filter_by(active=True).all()
    return render_template("inventory/form.html", title='Inventory', categories=categories)

@inventory.route('/save', methods=['POST'])
def save():

    flash('Inventory saved successfully')

    return redirect(url_for('inventory.index'))