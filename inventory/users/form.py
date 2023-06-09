from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired(), ])
    password = StringField('password', validators=[DataRequired()])
