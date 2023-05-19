from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..inventory.models import Inventory, InventoryStock
from ..stores.models import Store
from .models import Stocktake, StocktakeItem
import datetime
from ..db import db
stocktakes = Blueprint('stocktakes', __name__, url_prefix='/stock-takes')

@stocktakes.route('', methods=['GET'])
def index():
    stocktakeList = Stocktake.query.all()
    return render_template('stock-takes/index.html', title="Stock take", stocktakeList=stocktakeList)

@stocktakes.route('/form', methods=['GET'])
def form():
    inventory = Inventory.query.all()
    stores = Store.query.all()

    return render_template('stock-takes/form.html', title="Stock Take", inventory=inventory, stores=stores)

@stocktakes.route('/save', methods=['POST'])
def save():
    stocktake = Stocktake()
    stocktake.date = datetime.datetime.strptime(request.form.get('date'), "%Y-%m-%d").strftime("%Y-%m-%d")
    stocktake.store_id = request.form.get('store_id')
    db.session.add(stocktake)
    db.session.commit()

    for index, inv  in enumerate(request.form.getlist('id[]')):
        print("Qty - "+request.form.getlist('qty[]')[index])
        print("Inventory - "+inv)

        if(request.form.getlist('qty[]')[index]):
            stocktakeItem = StocktakeItem()
            stocktakeItem.qty = request.form.getlist('qty[]')[index]
            stocktakeItem.inventory_id = inv
            stocktakeItem.stocktake_id = stocktake.id
            db.session.add(stocktakeItem)
            db.session.commit()
    flash('Stock take saved successfully. Pending approval')

    return redirect(url_for('stocktakes.index'))

@stocktakes.route('/approve', methods=['POST'])
def approve():
    stocktake = Stocktake.query.filter_by(id=request.form.get('stock_take_id')).first_or_404()
    for item in stocktake.items:
        inventoryStock = InventoryStock.query.filter_by(inventory_id=item.inventory_id, store_id=stocktake.store_id).first()
        if not inventoryStock:
            inventoryStock = InventoryStock()
        totalQty = item.qty
        if inventoryStock.qty:
            totalQty = inventoryStock.qty + item.qty
        inventoryStock.store_id = stocktake.store_id
        inventoryStock.qty = totalQty
        inventoryStock.inventory_id = item.inventory_id
        inventoryStock.updated_at = datetime.datetime.utcnow()
        db.session.add(inventoryStock)
        db.session.commit()
    stocktake.status = 1
    db.session.add(stocktake)
    db.session.commit()
    flash("Stock take approved successfully")

    return redirect(url_for('stocktakes.index'))   

@stocktakes.route('/decline', methods=['POST'])
def decline():
    stocktake = Stocktake.query.filter_by(id=request.form.get('stock_take_id')).first_or_404()
    stocktake.status = 2
    db.session.add(stocktake)
    db.session.commit()
    flash("Stock take declined successfully")

    return redirect(url_for('stocktakes.index'))
 
@stocktakes.route('/delete', methods=['POST'])
def delete():
    stocktake = Stocktake.query.filter_by(id=request.form.get('stock_take_id')).first_or_404()

    db.session.delete(stocktake)
    db.session.commit()
    flash("Stock take deleted successfully")

    return redirect(url_for('stocktakes.index')) 

@stocktakes.app_template_filter()
def get_qty(stocks):

    return sum(list(map(lambda stk: stk.qty,stocks)))