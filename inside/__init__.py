import MySQLdb
from flask import Flask
from flaskext.mysql import MySQL
from flask_login import LoginManager
import pymysql

#app
app = Flask(__name__)
app.secret_key = 'ec9439cfc6c796ae2029594d'




# MySQL configurations
db = MySQL()
connection = MySQLdb.connect(host="localhost", user="root",password="123456",database="project_2")
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'project_2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
db.init_app(app)

#execute tables
conn = db.connect()
cursor = conn.cursor() # execute as list
cursor_dict = conn.cursor(pymysql.cursors.DictCursor) # execute as dict

#login
login_manager=LoginManager()
login_manager.init_app(app)


#blueprints
from .main.views import main_bp
from .lesson.views import lesson_bp
from .TestAndExercise.views import test_bp

app.register_blueprint(main_bp)
app.register_blueprint(lesson_bp)
app.register_blueprint(test_bp)

