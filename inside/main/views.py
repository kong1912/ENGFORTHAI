from flask import request, session, redirect, url_for, render_template
import pymysql 
import re 
from app import app
from inside import mysql
from flask import Blueprint

main_bp = Blueprint('main',__name__,template_folder='templates')

@main_bp.route('/')
def intro():
    if session.get('loggedin'):
        #return to home page if user has logged in
        return redirect(url_for('main.home'))
        

    return render_template('intro.html')



@main_bp.route('/login', methods=['GET', 'POST'])
def login():
 # connect
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
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
            # Redirect to home page
            #return 'Logged in successfully!'
            return redirect(url_for('main.home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    
    return render_template('login.html', msg=msg)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
 # connect
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
  
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        fullname = request.form.get('fullname')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
   
  #Check if account exists using MySQL
        cursor.execute('SELECT * FROM user WHERE username = %s', (username))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO user VALUES (NULL, %s, %s, %s, %s, NULL)', (fullname, username, password, email)) 
            conn.commit()
   
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('main.register', msg=msg)
  

@main_bp.route('/home')
def home():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    if 'loggedin' in session:
        cursor.execute('SELECT pretest_score FROM user WHERE id = %s ',(session['id']))
        score = cursor.fetchone()
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'],score=score)
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
 # Check if account exists using MySQL
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
  
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor.execute('SELECT * FROM user WHERE id = %s', [session['id']])
        user = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', user=user)
    # User is not loggedin redirect to login page
    return redirect(url_for('main.login'))





    