from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()

db = SQLAlchemy()

from .users.models import User
from .category.models import Category
from .inventory.models import Inventory
from .stores.models import Store
from .stocktakes.models import Stocktake, StocktakeItem

models = [
    User, Category, Inventory, Store, Stocktake, StocktakeItem
]
