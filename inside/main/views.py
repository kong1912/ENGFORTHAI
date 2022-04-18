from flask import request, redirect, url_for, render_template,flash, session
from flask_login import login_required, login_user, logout_user, current_user
from app import app
from inside import conn ,cursor, cursor_dict
from ..auth.forms import LoginForm, RegisterForm
from ..user import user_is_authenticated,get_user

from flask import Blueprint

main_bp = Blueprint('main',__name__,
                    template_folder='templates',
                    static_folder='static',static_url_path='/main/static')

@main_bp.route('/')
def intro():
    if user_is_authenticated():
        
        return render_template('intro.jinja')
    
    return render_template('intro.jinja')


 

@main_bp.route('/home')
def home():
    if user_is_authenticated():


    
        return render_template('home.jinja')
    else:
        return redirect(url_for('auth.login'))



@main_bp.route('/profile')
def profile(): 
    if user_is_authenticated():

        return render_template('profile.jinja')
    else:
        return redirect(url_for('auth.login'))






    