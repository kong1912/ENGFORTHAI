from flask_login import UserMixin
from inside import conn, cursor, db


class User(UserMixin):

    def __init__(self,username,password):
        self.username = username
        self.password = password



    def validate_password(self,password):
        cursor.execute('SELECT password FROM user WHERE password=%s',(password))
        user_password=cursor.fetchone()
        return user_password


    def select_user(self,username):
        cursor.execute('SELECT * FROM user WHERE username= %s',(username))
        user=cursor.fetchone()
        return user
    
    def get_id(self):
    
        cursor.execute(f'SELECT id FROM user WHERE email = %s',(self.email))
        user_id=cursor.fetchone()
        return user_id










