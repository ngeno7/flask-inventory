from ..db import db
import datetime

class Inventory(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    qty = db.Column(db.Numeric(12,2), nullable=False, default=0)
    min_level = db.Column(db.Numeric(12,2), nullable=False, default=0)
    reorder_level = db.Column(db.Numeric(12,2), nullable=False, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    #relationship
    
