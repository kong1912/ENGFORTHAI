from flask import request
from flask_login import UserMixin
from inside import db, conn, cursor, login_manager


class User(UserMixin):
    def __init__(self,password,email):
        self.password=password
        self.email=email

    def select_user(self,email):

        cursor.execute('SELECT * FROM user WHERE email="{}"'.format(email))
        user=cursor.fetchone()
        if user:
            id=user[0]
            return user
    
    def get_id(email):
        cursor=db.connection.cursor()
        cursor.execute('SELECT id FROM users WHERE email="{}"'.format(email))
        user_id=cursor.fetchone()
        if user_id:
            return user_id

    def insert_user(self,username,password,email):
        cursor=db.connection.cursor()
        cursor.execute('INSERT INTO users(username,password,email) VALUES(%s,%s,%s)',(self.username,self.password_hash,self.email))
        db.connection.commit()




@login_manager.user_loader
def load_user(user_id):
    return User.get_id(user_id)


