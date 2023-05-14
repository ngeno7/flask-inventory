from flask import Blueprint, render_template, request, redirect, flash, url_for
from .form import UserForm
from .models import User
from ..db import db

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('', methods=['GET', 'POST'])
def index():
    userform = UserForm()
    user = User()
    if request.method == 'POST' and userform.validate_on_submit():
        user.name = userform.name.data
        user.email = userform.username.data
        user.username = userform.username.data
        user.password = userform.password.data
        db.session.add(user)
        db.session.commit()
        flash('User saved successfully')

        return redirect(url_for('users.index'))
    users = User.query.all()

    return render_template("users/index.html", title="Users", form=userform, users=users)