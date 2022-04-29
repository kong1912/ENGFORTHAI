import json
from flask import Blueprint, redirect, url_for, render_template, jsonify, request, session
from app import conn, cursor, cursor_dict
from ..user import login_required
import random




test_bp = Blueprint('test', __name__,
                    template_folder='templates',
                    static_folder='static', 
                    static_url_path='/TestAndExercise/static')


@test_bp.route('/exercise_lesson1',methods=['GET', 'POST'])
@login_required
def exercise_lesson1():
    cursor.execute("SELECT word FROM word_list WHERE lesson = 1")
    words = cursor.fetchall()
    return render_template('exercise_lesson1.html.jinja', words=words)
    
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
    words = []
    cursor.execute("SELECT word FROM word_list WHERE stress = 1  LIMIT 3") #ORDER BY RAND()
    w1 = cursor.fetchall()
    cursor.execute("SELECT word FROM word_list WHERE stress = 2 LIMIT 3")
    w2 = cursor.fetchall()
    cursor.execute("SELECT word FROM word_list WHERE stress = 3 LIMIT 3")
    w3 = cursor.fetchall()
    cursor.execute("SELECT word FROM word_list WHERE stress = 4 LIMIT 3")
    w4 = cursor.fetchall()
    cursor.execute("SELECT word FROM word_list WHERE stress = 5 LIMIT 3")
    w5 = cursor.fetchall()
    words = w1 + w2 + w3 + w4 + w5
    # words = random.sample(words,len(words))
    return render_template('pretest.html.jinja',words=words)

@test_bp.route('/post-test')
def postteset():

    return render_template('posttest.html.jinja')

@test_bp.route('/result',methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        cursor.execute("INSERT INTO score (score) VALUES (%s) WHERE user_id = %s", (data['score'], session['u_id']))
        conn.commit()
        return jsonify(data)
    
    
    
        

    










