from flask import Blueprint, request, session, redirect, url_for, render_template
import pymysql
from inside import mysql
from flask import  Blueprint

lesson_bp = Blueprint('lesson',__name__,template_folder='templates')


@lesson_bp.route('/lesson1')
def lesson1():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson1 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('lesson1.html',data=data)


@lesson_bp.route('/lesson2')
def lesson2():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson2 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('lesson2.html',data=data)


@lesson_bp.route('/lesson3')
def lesson3():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson3 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('lesson2.html',data=data)

@lesson_bp.route('/lesson4')
def lesson4():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson4 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('lesson2.html',data=data)
    

@lesson_bp.route('/lesson5')
def lesson5():
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM lesson1 ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))
    
    
    
    return render_template('lesson2.html',data=data)



