import os
import uuid
from flask import Flask, redirect, session, url_for
from flaskext.mysql import MySQL
import pymysql

UPLOAD_FOLDER = 'files'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'UGWEGYWEY#(*T@#(*#@Y*(EFHEIGWHG'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# MySQL configurations
db = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'project_2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
db.init_app(app)

#execute tables
conn = db.connect()
cursor = conn.cursor() # execute as list
cursor_dict = conn.cursor(pymysql.cursors.DictCursor) # execute as dict


#blueprints
from .main.views import main_bp
from .lesson.views import lesson_bp
from .TestAndExercise.views import test_bp
from .auth.views import auth_bp

app.register_blueprint(main_bp)
app.register_blueprint(lesson_bp)
app.register_blueprint(test_bp)
app.register_blueprint(auth_bp)



