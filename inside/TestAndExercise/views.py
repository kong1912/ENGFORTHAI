from flask import Blueprint, request, session, redirect, url_for, render_template
import pymysql
from inside import mysql
test_bp = Blueprint('test', __name__,
                    template_folder='templates',
                    static_folder='static')


@test_bp.route('/exercise_lesson1')
def exercise_lesson1():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM word_list WHERE l_id = 1 ')
        data = cursor.fetchall()

        
        return render_template('exercise_lesson1.html',data=data)
        
    return render_template('login.html')
    
    
    
    

@test_bp.route('/exercise_lesson2')
def exercise_lesson2():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)  
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM word_list WHERE l_id = 2 ')
        data = cursor.fetchall()

        
        return render_template('exercise_lesson2.html',data=data)
       
    return render_template('login.html')
    
    
    
    

@test_bp.route('/exercise_lesson3')
def exercise_lesson3():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM word_list WHERE l_id = 3 ')
        data = cursor.fetchall()

        
        return render_template('exercise_lesson3.html',data=data)

    return render_template('login.html')
    
    
    
    

@test_bp.route('/exercise_lesson4')
def exercise_lesson4():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM word_list WHERE l_id = 4 ')
        data = cursor.fetchall()

        
        
        return render_template('exercise_lesson4.html',data=data)
    
    return render_template('login.html')
    
    
    
    

@test_bp.route('/exercise_lesson5')
def exercise_lesson5():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM word_list WHERE l_id = 5 ')
        data = cursor.fetchall()

        return render_template('exercise_lesson5.html',data=data)
    return render_template('login.html')


@test_bp.route('/pretest')
def pretest():
        
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)   
        if 'loggedin' in session:
            cursor.execute('SELECT * FROM pretest ')
            data = cursor.fetchall()
            
            # if request.method == 'POST':
            #     score = request.form.get('score')
            #     cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            #     conn.commit()
                
            #     return redirect(url_for('result'))
        
        
        
        return render_template('pretest.html',data=data)










