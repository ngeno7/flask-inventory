from flask import Flask
from .home.routes import home

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home)

    return app


create_app()