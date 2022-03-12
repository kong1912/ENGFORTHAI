from ctypes.wintypes import MSG
from flask import request, session, redirect, url_for, render_template, jsonify
import json
import pymysql 
import re 
from inside import app
from inside import mysql


@app.route('/login', methods=['GET', 'POST'])
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
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    
    return render_template('index.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
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
            cursor.execute('INSERT INTO user VALUES (NULL, %s, %s, %s, %s)', (fullname, username, password, email)) 
            conn.commit()
   
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)
  

@app.route('/')
def home():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    if 'loggedin' in session:
        cursor.execute('SELECT score FROM user WHERE id = %s ',(session['id']))
        score = cursor.fetchone()
        score = score['score']
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'],score=score)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))
  
# http://localhost:5000/logout - this will be the logout page
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))
 

@app.route('/profile')
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
    return redirect(url_for('login'))


@app.route('/pretest', methods=['POST','GET'])

def pretest():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM pretest ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))

        

       
        return render_template('pretest.html',data=data)
  
    return redirect(url_for('login'))


@app.route('/result', methods=['POST','GET'])
def result():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT score FROM user WHERE id = %s ',(session['id']))
        score = cursor.fetchone()
        score = score['score']
        return render_template('result.html',score=score)

    return redirect(url_for('login'))

@app.route('/posttest-beginner', methods=['POST','GET'])
def beginner():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM beginner ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))

        

       
        return render_template('posttest_beginner.html',data=data)
  
    return redirect(url_for('login'))

@app.route('/posttest-intermidiate', methods=['POST','GET'])
def intermediate():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM intermediate')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))

        

       
        return render_template('posttest_intermediate.html',data=data)
  
    return redirect(url_for('login'))

@app.route('/posttest-advanced', methods=['POST','GET'])
def expert():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM expert ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))

        

       
        return render_template('posttest_advanced.html',data=data)
  
    return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug=True)