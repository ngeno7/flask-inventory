from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired

class InventoryForm(FlaskForm):
    id = IntegerField('id',)
    name = StringField('name', validators=[DataRequired()])
    category_id = IntegerField('category_id', validators=[DataRequired()])
    reorder_level = FloatField('reorder_level', validators=[DataRequired()])
    min_level = FloatField('min_level', validators=[DataRequired()])
    description = StringField('description', validators=[])
