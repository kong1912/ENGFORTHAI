from flask_login import UserMixin
from inside import conn, cursor


class User(UserMixin):
    def __init__(self,username,password):
        
        self.username = username
        self.password = password


    def validate_password(self,password):
        cursor.execute(f'SELECT password FROM user WHERE password=%s',(password))
        user_password=cursor.fetchone()
        return user_password


    def select_user(self,username):
        cursor.execute(f'SELECT * FROM user WHERE username= %s',(username))
        user=cursor.fetchone()
        return user
    
    def get_id(self):
    
        cursor.execute(f'SELECT id FROM user' )
        user_id=cursor.fetchall()
        return user_id

    def insert_user(self,username,password,email):

        cursor.execute(f'INSERT INTO users (username,password,email) VALUES({username},{password},{email})')
        conn.commit()

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
        
    def is_anonymous(self):
        return False

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname







