from ..db import db
from flask_login import UserMixin
from ..db import login_manager
import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, default=True)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           default=datetime.datetime.utcnow)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))