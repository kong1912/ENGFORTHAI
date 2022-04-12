from flask_login import UserMixin
from . import conn, cursor, login_manager


class User(UserMixin):
    def __init__(self,username,password,email):
        
        self.username = username
        self.password = password
        self.email = email


    def validate_password(self,password):
        cursor.execute(f'SELECT password FROM users WHERE password={password}')
        user_password=cursor.fetchone()
        if user_password:
            return user_password


    def select_user(self,username):
        cursor.execute(f'SELECT * FROM user WHERE usrname={username}')
        user=cursor.fetchone()
        if user:
            return user
    
    def get_id(self,email):

        cursor.execute(f'SELECT id FROM users WHERE email={email}')
        user_id=cursor.fetchone()
        if user_id:
            return user_id

    def insert_user(self,username,password,email):

        cursor.execute(f'INSERT INTO users (username,password,email) VALUES({username},{password},{email})')
        conn.commit()



@login_manager.user_loader
def load_user(user_id):
    return User.get_id(user_id)


