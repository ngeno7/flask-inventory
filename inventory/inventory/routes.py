from flask import Blueprint, render_template

inventory = Blueprint('inventory', __name__, url_prefix='/inventory')

@inventory.route('')
def index():

    return render_template("inventory/index.html", title="Inventory")