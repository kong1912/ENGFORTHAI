import MySQLdb
from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.secret_key = 'ec9439cfc6c796ae2029594d'

mysql = MySQL()
   
# MySQL configurations
connection = MySQLdb.connect(host="localhost", user="root",password="123456",database="project_2")
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'project_2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

from .main.views import main_bp
from .lesson.views import lesson_bp
from .TestAndExercise.views import test_bp

app.register_blueprint(main_bp)
app.register_blueprint(lesson_bp)
app.register_blueprint(test_bp)