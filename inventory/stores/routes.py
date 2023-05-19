from flask import Blueprint, render_template, flash, url_for, redirect
from .form import StoreForm
from .models import Store
from ..db import db
stores = Blueprint('stores', __name__, url_prefix='/stores')

@stores.route('', methods=['POST', 'GET'])
def index():
    stores = Store.query.all()
    return render_template('stores/index.html', title="Stores", stores=stores)

@stores.route('/form', methods=[ 'GET' ])
def form():
    form = StoreForm()
    return render_template('stores/form.html', title="Stores", form=form)

@stores.route('/form/<id>', methods=[ 'GET' ])
def edit(id):
    form = StoreForm()
    store = Store.query.filter_by(id=id).first_or_404()

    form.id.data = store.id
    form.name.data = store.name
    form.description.data = store.description

    return render_template('stores/form.html', title="Stores", form=form)

@stores.route('/save', methods=[ 'POST' ])
def save():
    store = Store()
    form = StoreForm()
    if form.id.data:
        store = Store.query.filter_by(id=form.id.data).first_or_404()
    if form.validate_on_submit():
        store.name = form.name.data
        store.description = form.description.data
        store.active = True

        db.session.add(store)
        db.session.commit()

        flash('Store saved successfully')
    else:

        return render_template('stores/form.html', title="Stores", form=form)

    return redirect(url_for('stores.index'))
