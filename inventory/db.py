from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


from .users.models import User
from .category.models import Category
from .inventory.models import Inventory

models = [
    User, Category, Inventory
]