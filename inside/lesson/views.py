from flask import Blueprint, request,redirect, url_for, render_template
from inside import conn,cursor
from flask import  Blueprint

from ..user import user_is_authenticated


lesson_bp = Blueprint('lesson',__name__,
                        template_folder='templates',
                        static_folder='static',static_url_path='/lesson/static')



@lesson_bp.route('/lesson1')
def lesson1():
    if user_is_authenticated():

        return render_template('lesson1.jinja')
    else:
        return redirect(url_for('auth.login'))

    




@lesson_bp.route('/lesson2')
def lesson2():

    if user_is_authenticated():
    
        return render_template('lesson2.jinja')
    else:
        return redirect(url_for('auth.login'))
    


@lesson_bp.route('/lesson3')
def lesson3():
    if user_is_authenticated():
  
        return render_template('lesson3.jinja')  
    else:
        return redirect(url_for('auth.login'))





@lesson_bp.route('/lesson4')
def lesson4():
    if user_is_authenticated():
    

        return render_template('lesson2.jinja')
    else:
        return redirect(url_for('auth.login'))

 
    

@lesson_bp.route('/lesson5')
def lesson5():

    if user_is_authenticated():
    
        return render_template('lesson2.jinja')
    else:
        return redirect(url_for('auth.login'))





