from flask import session, redirect, url_for
from inside import conn, cursor, cursor_dict


class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def login_user(self):
        cursor_dict.execute('SELECT * FROM user WHERE username = %s and password = %s', (self.username, self.password))
        user = cursor_dict.fetchone()
        cursor_dict.execute('SELECT * FROM score WHERE u_id = %s', (user['u_id']))
        score = cursor_dict.fetchone()
        session['loggedin'] = True
        session['u_id'] = user['u_id']
        session['username'] = user['username']
        session['firstname'] = user['firstname']
        session['lastname'] = user['lastname']
        session['fullname'] = user['firstname'] + ' ' + user['lastname']
        session['email'] = user['email']
        session['pre_s'] = score['pre_s']
        session['post_s'] = score['post_s']
        session['l1_s'] = score['l1_s']
        session['l2_s'] = score['l2_s']
        session['l3_s'] = score['l3_s']
        session['l4_s'] = score['l4_s']
        session['l5_s'] = score['l5_s']
        return True

    
def logout_user():
    session.pop('loggedin')
    session.pop('u_id')
    session.pop('username')
    session.pop('firstname')
    session.pop('lastname')
    session.pop('email')
    session.pop('pre_s')
    session.pop('post_s')
    session.pop('l1_s')
    session.pop('l2_s')
    session.pop('l3_s')
    session.pop('l4_s')
    session.pop('l5_s')
    return True

def user_is_authenticated():
    return 'loggedin' in session

def get_user():
        cursor_dict.execute('SELECT * FROM user WHERE id = %s', (session['u_id']))
        user = cursor_dict.fetchone()
        return user









        
    







    










