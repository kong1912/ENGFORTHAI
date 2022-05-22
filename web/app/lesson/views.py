from flask import Blueprint, request,redirect, url_for, render_template
from app import conn,cursor
from flask import  Blueprint

from ..user import login_required


lesson_bp = Blueprint('lesson',__name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='/lesson/static')



@lesson_bp.route('/lesson1')
@login_required
def lesson1():
   
       return render_template('lesson1.html.jinja')



@lesson_bp.route('/lesson2')
@login_required
def lesson2():


    
    return render_template('lesson2.html.jinja')


@lesson_bp.route('/lesson3')
@login_required
def lesson3():

  
    return render_template('lesson3.html.jinja')  


@lesson_bp.route('/lesson4')
@login_required
def lesson4():

    

    return render_template('lesson4.html.jinja')


@lesson_bp.route('/lesson5')
@login_required
def lesson5():

   
    return render_template('lesson5.html.jinja')







