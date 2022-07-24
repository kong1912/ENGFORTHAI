import imp
from flask import request, redirect, url_for, render_template,flash, session
from app import conn ,cursor, cursor_dict
from ..user import login_required,get_user, user_is_authenticated, get_score
from flask import Blueprint



main_bp = Blueprint('main',__name__,
                    template_folder='templates',
                    static_folder='static',static_url_path='/main/static')

@main_bp.route('/')
def home():
    if user_is_authenticated():
        score = get_score()
        return render_template('home.html.jinja',score=score)
    return render_template('home.html.jinja')
    
@main_bp.route('/profile')
@login_required
def profile(): 
    user = get_user()
    score = get_score()
    return render_template('profile.html.jinja',user=user,score=score)
    
@main_bp.route('/course')
@login_required
def course():
    cursor.execute(f"SELECT pre_s FROM score WHERE u_id = {session['u_id']} ")
    pre_s = cursor.fetchone()

    return render_template('course.html.jinja',pre_s=pre_s)

@main_bp.route('/about')
def about():

    return render_template('about.html.jinja')

@main_bp.route('/coach')
@login_required
def coach():
    score = get_score()
    print(score['pre_s'])
    return render_template('coach.html.jinja',score=score)  

@main_bp.route('/info')
def info():
    
    return render_template('info.html.jinja')