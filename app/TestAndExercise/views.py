import json
from flask import Blueprint, redirect, url_for, render_template, jsonify
from requests import request
from app import conn, cursor, cursor_dict
from ..user import login_required

test_bp = Blueprint('test', __name__,
                    template_folder='templates',
                    static_folder='static', 
                    static_url_path='/TestAndExercise/static')


@test_bp.route('/exercise_lesson1',methods=['GET', 'POST'])
@login_required
def exercise_lesson1():

    cursor_dict.execute("SELECT word FROM word_list WHERE lesson = 1")
    words = cursor_dict.fetchall()
    print(words)
    for word in words():
        if request.form.method == "POST":         
            return render_template('exercise_lesson1.html.jinja',word=word.values())
    
    return render_template('exercise_lesson1.html.jinja',word=words[0])
    
    

@test_bp.route('/exercise_lesson2')
@login_required
def exercise_lesson2():

    cursor.execute("SELECT word FROM word_list WHERE lesson = 2")
    words = cursor.fetchall()
        
    return render_template('exercise_lesson2.html.jinja',words=words)
  

@test_bp.route('/exercise_lesson3')
@login_required
def exercise_lesson3():

    cursor.execute("SELECT word FROM word_list WHERE lesson = 3")
    words = cursor.fetchall()

    return render_template('exercise_lesson3.html.jinja',words=words)


@test_bp.route('/exercise_lesson4')
@login_required
def exercise_lesson4():
    cursor.execute("SELECT word FROM word_list WHERE lesson = 4")
    words = cursor.fetchall()
    
    return render_template('exercise_lesson4.html.jinja',words=words)
    
@test_bp.route('/exercise_lesson5')
@login_required
def exercise_lesson5():
    cursor.execute("SELECT word FROM word_list WHERE lesson = 5")
    words = cursor.fetchall()

    return render_template('exercise_lesson5.html.jinja',words=words)
    
@test_bp.route('/pre-test')
def pretest():
    


    return render_template('pretest.html.jinja')

@test_bp.route('/post-test')
def postteset():

    return render_template('posttest.html.jinja')


    










