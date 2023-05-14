from flask import Flask
from flask_migrate import Migrate

from .db import db
from .home.routes import home
from .users.routes import users
from .category.routes import categories
from .inventory.routes import inventory

from .db import models

migrate = Migrate()
#db config to be moved to .env
DB_USER = "postgres"
DB_PASS = "root"
DB_NAME = "inventory"
DB_HOST = "localhost"

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
    app.config['SECRET_KEY'] = 'FBzsisRFjlL5mV54DEf5so1xxbL5ZiY6TIEAUY3s'
    app.register_blueprint(home)
    app.register_blueprint(users)
    app.register_blueprint(categories)
    app.register_blueprint(inventory)
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)

    return app

create_app()