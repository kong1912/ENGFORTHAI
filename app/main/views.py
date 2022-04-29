from flask import request, redirect, url_for, render_template,flash, session
from app import app
from app import conn ,cursor, cursor_dict
from ..user import login_required,get_user, user_is_authenticated

from flask import Blueprint

main_bp = Blueprint('main',__name__,
                    template_folder='templates',
                    static_folder='static',static_url_path='/main/static')

@main_bp.route('/')
def intro():
    if user_is_authenticated():
        return redirect(url_for('main.home'))

    return render_template('intro.html.jinja')
    
@main_bp.route('/home')
@login_required
def home():

    return render_template('home.html.jinja')
    
@main_bp.route('/profile')
@login_required
def profile(): 

    user = get_user()
    return render_template('profile.html.jinja',user=user)
    
@main_bp.route('/course')
@login_required
def course():

    return render_template('course.html.jinja')
    







    