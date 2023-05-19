from flask import Blueprint, render_template, url_for, redirect, flash, request
from ..category.models import Category
from .form import InventoryForm
from .models import Inventory
from ..db import db

inventory = Blueprint('inventory', __name__, url_prefix='/inventory')

@inventory.route('', methods=['GET'])
def index():
    inventory = Inventory.query.all()
    return render_template("inventory/index.html", title="Inventory", inventory=inventory)

@inventory.route('/form', methods=['GET', 'POST'])
def form():
    categories = Category.query.filter_by(active=True).all()
    form= InventoryForm()

    return render_template("inventory/form.html", title='Inventory', form=form, categories=categories)

@inventory.route('/form/<id>', methods=['GET', 'POST'])
def edit(id):
    inventory = Inventory.query.filter_by(id=id).first_or_404()
    form= InventoryForm()
    if inventory:
        form.id.data = inventory.id
        form.name.data = inventory.name
        form.description.data = inventory.description
        form.category_id.data = inventory.category_id
        form.reorder_level.data = inventory.reorder_level
        form.min_level.data = inventory.min_level
    categories = Category.query.filter_by(active=True).all()

    return render_template("inventory/form.html", title='Inventory', form=form, categories=categories)

@inventory.route('/save', methods=['POST'])
def save():
    inventory = Inventory()
    form = InventoryForm()
    if form.validate_on_submit():
        if(request.form.get('id')):
            inventory = Inventory.query.filter_by(id=request.form.get('id')).first_or_404()

        inventory.name = form.name.data
        inventory.description = form.description.data
        inventory.category_id = form.category_id.data
        inventory.reorder_level = form.reorder_level.data
        inventory.min_level = form.min_level.data

        db.session.add(inventory)
        db.session.commit()
    else: 
        for error in form.errors:
                print(error)
        categories = Category.query.filter_by(active=True).all()

        return render_template("inventory/form.html", title='Inventory', form=form, categories=categories)

    flash('Inventory saved successfully')

    return redirect(url_for('inventory.index'))
