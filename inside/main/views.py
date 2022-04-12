from flask import request, session, redirect, url_for, render_template
from flask_login import login_required, login_user, logout_user, current_user
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
        user = User


    



    
    
    
    return render_template('login.jinja')

@main_bp.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()




  
    return render_template('register.jinja')
  
@login_required
@main_bp.route('/home')
def home():

   
    cursor.execute('SELECT * FROM user WHERE id = %s ',(session['id']))
        score = cursor.fetchone()
        return render_template('home.jinja', username=session['username'])


  

@main_bp.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('main.intro'))
 
@login_required
@main_bp.route('/profile')
def profile(): 

    
        cursor.execute('SELECT * FROM user WHERE id = %s', [session['id']])
        user = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.jinja', user=user)
    # User is not loggedin redirect to login page
    return redirect(url_for('main.login'))





    