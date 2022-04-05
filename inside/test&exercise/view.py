from django import views
from flask import Blueprint, request, session, redirect, url_for, render_template
import pymysql
from app import app
from inside import mysql

view = Blueprint('view',__name__,
                template_folder='templates/owners')


@view.route('/pretest', methods=['POST','GET'])
def pretest():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM pretest ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))

        

       
        return render_template('pretest.html',data=data)
  
    return redirect(url_for('login'))


@view.route('/result', methods=['POST','GET'])
def result():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT score FROM user WHERE id = %s ',(session['id']))
        score = cursor.fetchone()
        score = score['score']
        return render_template('result.html',score=score)

    return redirect(url_for('login'))

@view.route('/posttest-beginner', methods=['POST','GET'])
def beginner():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM beginner ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))

        

       
        return render_template('posttest_beginner.html',data=data)
  
    return redirect(url_for('login'))

@view.route('/posttest-intermidiate', methods=['POST','GET'])
def intermediate():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM intermediate_')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            print(score)
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))

        

       
        return render_template('posttest_intermediate.html',data=data)
  
    return redirect(url_for('login'))

@app.route('/posttest-expert', methods=['POST','GET'])
def expert():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)   
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM expert ')
        data = cursor.fetchall()
        
        if request.method == 'POST':
            score = request.form.get('score')
            cursor.execute('UPDATE user SET score = %s WHERE id = %s', (score, session['id']))
            conn.commit()
            
           
            return redirect(url_for('result'))

        

       
        return render_template('posttest_expert.html',data=data)
  
    return redirect(url_for('login'))

print("Hello my name is windton I'm 24 year old")








