from flask import session, redirect, url_for
from inside import conn, cursor, cursor_dict


class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = None
        self.firstname = None
        self.lastname = None
        self.email = None

        
    def select_user(self,username):
        cursor_dict.execute('SELECT * FROM user WHERE username = %s', (username))
        user = cursor.fetchone()

        return user

    def login_user(self):
        cursor_dict.execute('SELECT * FROM user WHERE username = %s and password = %s', (self.username, self.password))
        user = cursor_dict.fetchone()
        session['loggedin'] = True
        session['id'] = user['id']
        session['username'] = user['username']
        
        return True

    def is_authenticated(self):
        if session['loggedin'] == True:
            return True

def logout_user():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return True

def login_required():

    if session['loggedin']:
        return True
    else:
        return redirect(url_for('auth.login'))



    








        
    







    










