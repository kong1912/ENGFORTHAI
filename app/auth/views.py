from dataclasses import field
from colorama import Cursor
from flask import request, redirect, url_for, render_template,flash,Blueprint
from app import app
from app import conn , cursor
from ..auth.forms import LoginForm, RegisterForm
from ..user import User, logout_user


auth_bp = Blueprint('auth',__name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/auth/static')




@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()
    
    if form.validate_on_submit():
        cursor.execute('INSERT INTO user (email,firstname,lastname,username,password) VALUES(%s,%s,%s,%s,%s)',
        (form.email.data,form.firstname.data,form.lastname.data,form.username.data,form.password.data))
        conn.commit()
        cursor.execute("INSERT INTO score (u_id) SELECT u_id FROM user WHERE username = %s", (form.username.data))
        conn.commit()
        user = User(form.username.data, form.password.data)
        user.login_user()
        return redirect(url_for('main.home'))

    
    return render_template('register.html.jinja', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User(form.username.data,form.password.data)
        user.login_user()
        return redirect(url_for('main.home'))

    return render_template('login.html.jinja', form=form)

@auth_bp.route('/logout')
def logout():
    
    logout_user()
    return redirect(url_for('main.intro'))
    