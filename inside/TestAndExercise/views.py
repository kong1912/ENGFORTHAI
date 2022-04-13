import json
from flask import Blueprint, request, session, redirect, url_for, render_template
import pymysql
from inside import conn, cursor, cursor_dict

test_bp = Blueprint('test', __name__,
                    template_folder='templates',
                    static_folder='static', static_url_path='/TestAndExercise/static')


@test_bp.route('/exercise_lesson1')
def exercise_lesson1():
    


        
    return render_template('exercise_lesson1.jinja')
        

    
    
    
    

@test_bp.route('/exercise_lesson2')
def exercise_lesson2():
    
    
    return render_template('exercise_lesson2.jinja')
       

    
    
    
    

@test_bp.route('/exercise_lesson3')
def exercise_lesson3():
    



        
    return render_template('exercise_lesson3.jinja')


    
    
    
    

@test_bp.route('/exercise_lesson4')
def exercise_lesson4():
    
  


        
        
    return render_template('exercise_lesson4.jinja')
    

    
    
    
    

@test_bp.route('/exercise_lesson5')
def exercise_lesson5():
    


    return render_template('exercise_lesson5.jinja')
    


@test_bp.route('/pretest')
def pretest():
        


    return render_template('pretest.jinja')
    










