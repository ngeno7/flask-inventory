from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class InventoryForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    category_id = IntegerField('category_id', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired(),])
