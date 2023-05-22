from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user

from passlib.hash import pbkdf2_sha256
from ..users.models import User

login = Blueprint('login', __name__,)

@login.route('/login', methods=[ 'GET', 'POST', ])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and pbkdf2_sha256.verify(password, user.password):
           login_user(user)
           return redirect(url_for('home.index'))

    return render_template('auth/login.html')

@login.route('/logout', methods=[ 'POST'])
def logout():
    if request.method == 'POST':
        logout_user()
        return redirect(url_for('login.index'))

    return redirect(url_for('login.index'))