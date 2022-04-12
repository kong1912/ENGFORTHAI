from flask import request, session, redirect, url_for, render_template
from flask_login import login_required, login_user, logout_user, current_user,flash
from app import app
from inside import conn ,cursor, cursor_dict
from ..forms import LoginForm, RegisterForm
from ..user import User

from flask import Blueprint

main_bp = Blueprint('main',__name__,
                    template_folder='templates',
                    static_folder='static',static_url_path='/main/static')

@main_bp.route('/')
def intro():
    
    return render_template('intro.jinja')



@main_bp.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.select_user(form.username.data)
        if user is not None and user.validate_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.intro'))

    return render_template('login.jinja', form=form)


@main_bp.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.password.data, form.email.data)
        user.insert_user()
        login_user(user)
        return redirect('main.login')

    return render_template('register.jinja', form=form)
 
@login_required
@main_bp.route('/home')
def home():

   
    return render_template('home.jinja')


  
@main_bp.route('/logout')
def logout():

    logout_user()
    flash('You have been logged out')

    return redirect(url_for('main.intro'))
 
@login_required
@main_bp.route('/profile')
def profile(): 


    return render_template('profile.jinja', user=user)






    