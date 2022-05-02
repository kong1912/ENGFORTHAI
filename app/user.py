from flask import session, url_for, redirect, flash
from app import conn, cursor, cursor_dict
from functools import wraps


class User():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login_user(self):
        cursor_dict.execute('SELECT * FROM user WHERE username = %s AND password = %s',(self.username, self.password))
        user = cursor_dict.fetchone()
        session['loggedin'] = True
        for key, value in user.items():
            session[key] = value
            
        cursor_dict.execute("SELECT * FROM score WHERE u_id = %s", (session['u_id']))   
        score = cursor_dict.fetchone()
        for key, value in score.items():
            session[key] = value
    
def logout_user():
    user = get_user()
    session.pop('loggedin', None)
    for key in user.items():
        session.pop(key, None)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'loggedin' in session:
            return f(*args, **kwargs)
        else:
            flash('กรุณา login', 'danger')
            return redirect(url_for('auth.login'))
    return wrap

def user_is_authenticated():
    return 'loggedin' in session

def get_user():
    cursor_dict.execute('SELECT * FROM user WHERE u_id = %s', (session['u_id']))
    user = cursor_dict.fetchone()
    return user

def get_score():
    cursor_dict.execute('SELECT * FROM score WHERE u_id = %s', (session['u_id']))
    score = cursor_dict.fetchone()
    return score
