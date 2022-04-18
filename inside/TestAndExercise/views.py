import json
from flask import Blueprint, request, session, redirect, url_for, render_template
import pymysql
from inside import conn, cursor, cursor_dict

test_bp = Blueprint('test', __name__,
                    template_folder='templates',
                    static_folder='static', static_url_path='/TestAndExercise/static')


@test_bp.route('/exercise_lesson1')
def exercise_lesson1():
    
    cursor.execute("SELECT word FROM word_list WHERE l_id = 1")
    words = cursor.fetchall()


    return render_template('exercise_lesson1.jinja',words=words)
        

    
    
    
    

@test_bp.route('/exercise_lesson2')
def exercise_lesson2():
    cursor.execute("SELECT word FROM word_list WHERE l_id = 2")
    words = cursor.fetchall()
    
    
    return render_template('exercise_lesson2.jinja',words=words)
       

    
    
    
    

@test_bp.route('/exercise_lesson3')
def exercise_lesson3():
    cursor.execute("SELECT word FROM word_list WHERE l_id = 1")
    words = cursor.fetchall()

        
    return render_template('exercise_lesson3.jinja',words=words)


    
    
    
    

@test_bp.route('/exercise_lesson4')
def exercise_lesson4():
    cursor.execute("SELECT word FROM word_list WHERE l_id = 1")
    words = cursor.fetchall()
    
  
    return render_template('exercise_lesson4.jinja',words=words)
    

    
    
    
    

@test_bp.route('/exercise_lesson5')
def exercise_lesson5():
    cursor.execute("SELECT word FROM word_list WHERE l_id = 1")
    words = cursor.fetchall()
    


    return render_template('exercise_lesson5.jinja',words=words)
    


@test_bp.route('/pretest')
def pretest():
    
    cursor.execute("SELECT word FROM word_list WHERE l_id = 1")
    words = cursor.fetchall()


    return render_template('pretest.jinja',words=words)
    










