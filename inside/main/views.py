from flask import request, redirect, url_for, render_template,flash
from flask_login import login_required, login_user, logout_user, current_user
from app import app
from inside import conn ,cursor, cursor_dict
from ..auth.forms import LoginForm, RegisterForm
from ..auth.user import User

from flask import Blueprint

main_bp = Blueprint('main',__name__,
                    template_folder='templates',
                    static_folder='static',static_url_path='/main/static')

@main_bp.route('/')
def intro():
    #return to home page if user has logged in

    return render_template('intro.jinja')


 
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


    return render_template('profile.jinja')






    