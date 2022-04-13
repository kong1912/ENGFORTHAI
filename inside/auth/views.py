from colorama import Cursor
from flask import request, redirect, url_for, render_template,flash,Blueprint
from flask_login import login_required, login_user, logout_user, current_user
from app import app
from inside import conn , cursor
from ..auth.forms import LoginForm, RegisterForm
from ..auth.user import User


auth_bp = Blueprint('auth',__name__,
                    template_folder='templates',
                    static_folder='static',static_url_path='/auth/static')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User(form.username.data, form.password.data)
        user.select_user(form.username.data)
        if user is not None and user.validate_password(form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('main.home'))

    return render_template('login.jinja', form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()
    
    if form.validate_on_submit():
        cursor.execute('INSERT INTO users (email,firstname,lastname,username,password) VALUES(%s,%s,%s,%s,%s)',
        (form.email.data,form.firstname.data,form.lastname.data,form.username.data,form.password.data))
        conn.commit()
        user = User(form.username.data, form.password.data)
        user.select_user
        login_user(user)
        return redirect(url_for('main.home'))
    return render_template('register.jinja', form=form)