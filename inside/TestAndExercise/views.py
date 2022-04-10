from flask import Blueprint, request, session, redirect, url_for, render_template
import pymysql
from inside import mysql,conn,cursor
from inside.function import user_has_loggedin
test_bp = Blueprint('test', __name__,
                    template_folder='templates',
                    static_folder='static')


@test_bp.route('/exercise_lesson1')
def exercise_lesson1():
    

    if user_has_loggedin():
        cursor.execute('SELECT * FROM word_list WHERE l_id = 1 ')
        data = cursor.fetchall()

        
        return render_template('exercise_lesson1.html',data=data)
        
    return redirect('main.login')
    
    
    
    

@test_bp.route('/exercise_lesson2')
def exercise_lesson2():
    
 
    if user_has_loggedin():
        cursor.execute('SELECT * FROM word_list WHERE l_id = 2 ')
        data = cursor.fetchall()

        
        return render_template('exercise_lesson2.html',data=data)
       
    return redirect('main.login')
    
    
    
    

@test_bp.route('/exercise_lesson3')
def exercise_lesson3():
    

    if user_has_loggedin():
        cursor.execute('SELECT * FROM word_list WHERE l_id = 3 ')
        data = cursor.fetchall()

        
        return render_template('exercise_lesson3.html',data=data)

    return redirect('main.login')
    
    
    
    

@test_bp.route('/exercise_lesson4')
def exercise_lesson4():
    
  
    if user_has_loggedin():
        cursor.execute('SELECT * FROM word_list WHERE l_id = 4 ')
        data = cursor.fetchall()

        
        
        return render_template('exercise_lesson4.html',data=data)
    
    return redirect('main.login')
    
    
    
    

@test_bp.route('/exercise_lesson5')
def exercise_lesson5():
    

    if user_has_loggedin():
        cursor.execute('SELECT * FROM word_list WHERE l_id = 5 ')
        data = cursor.fetchall()

        return render_template('exercise_lesson5.html',data=data)
    
    return redirect('main.login')


@test_bp.route('/pretest')
def pretest():
        

    if user_has_loggedin():
        cursor.execute('SELECT * FROM pretest ')
        data = cursor.fetchall()

        return render_template('pretest.html',data=data)
    
    return redirect('main.login')










