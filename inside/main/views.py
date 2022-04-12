from flask import request, session, redirect, url_for, render_template

from flask_login import login_required, login_user, logout_user, current_user
from app import app
from inside import mysql,conn,cursor
from inside.function import user_has_loggedin
from flask import Blueprint

main_bp = Blueprint('main',__name__,
                    template_folder='templates',
                    static_folder='static',static_url_path='/main/static')

@main_bp.route('/')
def intro():
    if user_has_loggedin():
        
        return redirect(url_for('main.home'))
        

    return render_template('intro.jinja')



@main_bp.route('/login', methods=['GET', 'POST'])
def login():


    
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form.get('username')
        password = request.form.get('password')
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
   
    # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('main.home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    
    return render_template('login.jinja', msg=msg)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():



  
    return render_template('register.jinja')
  
@login_required
@main_bp.route('/home')
def home():

    if user_has_loggedin():
        cursor.execute('SELECT * FROM user WHERE id = %s ',(session['id']))
        score = cursor.fetchone()
        # User is loggedin show them the home page
        return render_template('home.jinja', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('main.login'))
  
# http://localhost:5000/logout - this will be the logout page
@main_bp.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('main.intro'))
 

@main_bp.route('/profile')
def profile(): 

    # Check if user is loggedin
    if user_has_loggedin():
        # We need all the account info for the user so we can display it on the profile page
        cursor.execute('SELECT * FROM user WHERE id = %s', [session['id']])
        user = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.jinja', user=user)
    # User is not loggedin redirect to login page
    return redirect(url_for('main.login'))





    