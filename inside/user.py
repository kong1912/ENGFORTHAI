from flask import request
from flask_login import UserMixin
from inside import db, conn, cursor, login_manager


class User(UserMixin):
    def __init__(self,username,password,email):
        
        self.username = username
        self.password = password
        self.email = email


    def select_user(self,email):

        cursor.execute(f'SELECT * FROM user WHERE email={email}')
        user=cursor.fetchone()
        if user:
            id=user[0]
            return user
    
    def get_id(self,email):

        cursor.execute(f'SELECT id FROM users WHERE email={email}')
        user_id=cursor.fetchone()
        if user_id:
            return user_id

    def insert_user(self,username,password,email):

        cursor.execute(f'INSERT INTO users (username,password,email) VALUES({username},{password},{email})')
        db.connection.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.get_id(user_id)


