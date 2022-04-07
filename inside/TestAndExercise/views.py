from flask import Blueprint, request, session, redirect, url_for, render_template
import pymysql
from inside import mysql
test_bp = Blueprint('test', __name__,
        template_folder='templates')


@test_bp.route('/exercise_lesson1')
def exercise_lesson1():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        
        return render_template('exercise_lesson1.html')
        
        
    return render_template('login.html')
    
    
    
    

@test_bp.route('/exercise_lesson2')
def exercise_lesson2():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)  
    if 'loggedin' in session:
        
        return render_template('exercise_lesson2.html')
       
    return render_template('login.html')
    
    
    
    

@test_bp.route('/exercise_lesson3')
def exercise_lesson3():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        
        return render_template('exercise_lesson3.html')
    return render_template('login.html')
    
    
    
    

@test_bp.route('/exercise_lesson4')
def exercise_lesson4():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT lesson4 FROM user')
        
        
        return render_template('exercise_lesson4.html')
    
    return render_template('login.html')
    
    
    
    

@test_bp.route('/exercise_lesson5')
def exercise_lesson5():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        # execute mysql query from lesson1
        cursor.execute('SELECT lesson5 FROM user')
        data = cursor.fetchall()


        return render_template('exercise_lesson5.html')
    return render_template('login.html')


@test_bp.route('/pretest')
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










