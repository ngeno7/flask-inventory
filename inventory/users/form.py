from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Unique
from .models import User

class UserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired(), Unique(User.username, get_session=lambda: session) ])
    password = StringField('password', validators=[DataRequired()])
