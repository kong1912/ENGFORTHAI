import json
from flask import Blueprint, request, session, redirect, url_for, render_template
import pymysql
from app import conn, cursor, cursor_dict
from ..user import user_is_authenticated

test_bp = Blueprint('test', __name__,
                    template_folder='templates',
                    static_folder='static', 
                    static_url_path='/TestAndExercise/static')


@test_bp.route('/exercise_lesson1')
def exercise_lesson1():
    if user_is_authenticated():
    
        cursor.execute("SELECT word FROM word_list WHERE lesson = 1")
        words = cursor.fetchall()


        return render_template('exercise_lesson1.html.jinja',words=words)
    
    return redirect(url_for('auth.login'))    

    
    
    
    

@test_bp.route('/exercise_lesson2')
def exercise_lesson2():
    if user_is_authenticated():
        cursor.execute("SELECT word FROM word_list WHERE lesson = 2")
        words = cursor.fetchall()
        
        return render_template('exercise_lesson2.html.jinja',words=words)
    return redirect(url_for('auth.login'))   

    
    
@test_bp.route('/exercise_lesson3')
def exercise_lesson3():
    if user_is_authenticated():
        cursor.execute("SELECT word FROM word_list WHERE lesson = 3")
        words = cursor.fetchall()

        
        return render_template('exercise_lesson3.html.jinja',words=words)
    return redirect(url_for('auth.login'))

    
    
    
    

@test_bp.route('/exercise_lesson4')
def exercise_lesson4():
    cursor.execute("SELECT word FROM word_list WHERE lesson = 3")
    words = cursor.fetchall()
    
  
    return render_template('exercise_lesson4.html.jinja',words=words)
    

    
    
    
    

@test_bp.route('/exercise_lesson5')
def exercise_lesson5():
    cursor.execute("SELECT word FROM word_list WHERE lesson = 5")
    words = cursor.fetchall()
    


    return render_template('exercise_lesson5.html.jinja',words=words)
    


@test_bp.route('/pretest')
def pretest():
    


    return render_template('pretest.html.jinja')
    










