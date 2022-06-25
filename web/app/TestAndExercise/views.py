import json
import os
import math
import pathlib
import subprocess
import sys
import uuid
import pandas as pd
import torch
import torch.nn.functional as F
import torchaudio
from torch import nn
from torch.utils.data import Dataset
from flask import Blueprint, redirect, url_for, render_template, jsonify, request, session, flash
from app import conn, cursor, cursor_dict, app, VAR_DIR, LOG_DIR, CACHE_DIR, \
UPLOAD_DIR, ANNOTATIONS_FILE, AUDIO_DIR,MODEL_FILE,ANNOTATIONS_FILE_TEST 
from ..user import login_required



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
    cursor.execute("SELECT word FROM word_list WHERE lesson = 1")
    words = cursor.fetchall()

    return render_template('pretest.html.jinja',words=words)

@test_bp.route('/post-test')
def postteset():

    return render_template('posttest.html.jinja')

@test_bp.route('/insert_score',methods=['POST'])
def insert_score():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        cursor.execute(f"INSERT INTO score (s1_s,s2_s,s3_s,s4_s,s5_s) \
                         VALUES ({data[0].score},{data[1].score},{data[2].score},{data[3].score},{data[4].score})")
        conn.commit()
        return jsonify({})

@test_bp.route('/result')
def result():
    cursor.execute("SELECT pre_s FROM score WHERE u_id = %s", (session['u_id']))
    pre_s = cursor.fetchone()
    cursor_dict.execute("SELECT s1_s,s2_s,s3_s,s4_s,s5_s FROM score WHERE u_id = %s", (session['u_id']))
    stress = cursor_dict.fetchone()
    print(stress)
    # sort stress ascending
    stress = sorted(stress, key=lambda x: x[1:])
    print(stress)
    return render_template('result.html.jinja',stress=stress,pre_s=pre_s)

