from flask import Blueprint, request,redirect, url_for, render_template
from inside import conn,cursor
from flask import  Blueprint

from inside.function import user_has_loggedin

lesson_bp = Blueprint('lesson',__name__,
                        template_folder='templates',
                        static_folder='static')



@lesson_bp.route('/lesson1')
def lesson1():
      
    if user_has_loggedin():
        
        return render_template('lesson1.html')
    
    return redirect('main.login')



@lesson_bp.route('/lesson2')
def lesson2():
      
    if user_has_loggedin():
        
    
        return render_template('lesson2.html')
    
    return redirect('main.login')


@lesson_bp.route('/lesson3')
def lesson3():
      
    if user_has_loggedin():
        
        
        return render_template('lesson3.html')  

    return redirect('main.login')

@lesson_bp.route('/lesson4')
def lesson4():
    
    if user_has_loggedin():
       return render_template('lesson2.html')
    
    return redirect('main.login')

    
    
    

@lesson_bp.route('/lesson5')
def lesson5():
    
    if user_has_loggedin():
        
        return render_template('lesson2.html')

    return redirect('main.login')



