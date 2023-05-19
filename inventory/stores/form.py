from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class StoreForm(FlaskForm):
    id = IntegerField('id')
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[])
