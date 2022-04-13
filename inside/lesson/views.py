from flask import Blueprint, request,redirect, url_for, render_template
from flask_login import login_required
from inside import conn,cursor
from flask import  Blueprint


lesson_bp = Blueprint('lesson',__name__,
                        template_folder='templates',
                        static_folder='static',static_url_path='/lesson/static')


@login_required
@lesson_bp.route('/lesson1')
def lesson1():
      

        
    return render_template('lesson1.jinja')



@login_required
@lesson_bp.route('/lesson2')
def lesson2():
      

        
    
    return render_template('lesson2.jinja')
    

@login_required
@lesson_bp.route('/lesson3')
def lesson3():
      

        
        
    return render_template('lesson3.jinja')  



@login_required
@lesson_bp.route('/lesson4')
def lesson4():
    

    return render_template('lesson2.jinja')
    


    
    
    
@login_required
@lesson_bp.route('/lesson5')
def lesson5():
    

        
    return render_template('lesson2.jinja')





