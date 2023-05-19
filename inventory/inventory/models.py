from ..db import db
import datetime

class Inventory(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    qty = db.Column(db.Numeric(12,2), nullable=True, default=0)
    min_level = db.Column(db.Numeric(12,2), nullable=True, default=0)
    reorder_level = db.Column(db.Numeric(12,2), nullable=True, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    #relationship
    category = db.relationship("Category", backref="categories")
    stocks = db.relationship('InventoryStock', backref="inventory_stocks")

class InventoryStock(db.Model):
    __tablename__ = 'inventory_stocks'

    id = db.Column(db.Integer, primary_key=True)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    qty = db.Column(db.Numeric(12,2), default=0, nullable=True)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
