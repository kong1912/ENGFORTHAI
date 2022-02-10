
from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__) 
app.secret_key = 'ec9439cfc6c796ae2029594d'

mysql = MySQL()
   
# MySQL configurations


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'project_2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

from inside import routes