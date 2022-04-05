from ctypes.wintypes import MSG
from flask import request, session, redirect, url_for, render_template, jsonify
import pymysql 
import re 
from app import app
from inside import mysql


@app.route('/login2')
def login2():


    return render_template('login2.html')






@app.route('/')
def intro():
    
    return render_template('intro.html')





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
    
    return render_template('login.html', msg=msg)

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
            cursor.execute('INSERT INTO user VALUES (NULL, %s, %s, %s, %s, NULL)', (fullname, username, password, email)) 
            conn.commit()
   
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)
  

@app.route('/home')
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
   return redirect(url_for('intro'))
 

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




@app.route('/lesson1')
def lesson1():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson1 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('lesson1.html',data=data)


@app.route('/lesson2')
def lesson2():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson2 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('lesson2.html',data=data)


@app.route('/lesson3')
def lesson3():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson3 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('lesson2.html',data=data)

@app.route('/lesson4')
def lesson4():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson4 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('lesson2.html',data=data)
    

@app.route('/lesson5')
def lesson5():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson1 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('lesson2.html',data=data)
    
    
@app.route('/exercise_lesson1')
def exercise_lesson1():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson1 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('exercise_lesson1.html',data=data)

@app.route('/exercise_lesson2')
def exercise_lesson2():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson1 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('exercise_lesson2.html',data=data)

@app.route('/exercise_lesson3')
def exercise_lesson3():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson1 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('exercise_lesson3.html',data=data)

@app.route('/exercise_lesson4')
def exercise_lesson4():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson1 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('exercise_lesson4.html',data=data)

@app.route('/exercise_lesson5')
def exercise_lesson5():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson1 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('exercise_lesson5.html',data=data)






if __name__ == '__main__':
	app.run(debug=True)