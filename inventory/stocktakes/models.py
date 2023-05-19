from ..db import db
from ..stores.models import Store
import datetime

class Stocktake(db.Model):
    __tablename__ = 'stock_takes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    status = db.Column(db.Integer, nullable=True, default=0)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    #relationship
    items = db.relationship("StocktakeItem", backref="stock_takes", cascade="all, delete")
    store = db.relationship("Store", backref="stores")
    if status == 0:
        status_name = db.column_property('Pending')
    else:
        status_name = db.column_property('Approved')
           

class StocktakeItem(db.Model):
    __tablename__ = 'stock_take_items'

    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Numeric(12,2), nullable=True, default=0)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    stocktake_id = db.Column(db.Integer, db.ForeignKey('stock_takes.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    # relationship
    inventory = db.relationship("Inventory", backref="inventory")
