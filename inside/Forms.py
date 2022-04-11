from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from inside import conn, cursor



class RegisterForm(FlaskForm):
    def check_username(self, username):
        cursor.execute('SELECT username FROM user WHERE username = %s', username)
        data = cursor.fetchone()
        if data:
            raise validators.ValidationError('Username is already taken')
        

    
    fullname = StringField(Label='Full Name', validators=[DataRequired()])
    username = StringField(Label='Username', validators=[DataRequired()])
    password = PasswordField(Label='Password', validators=[DataRequired()])
    submit = SubmitField(Label='สมัครสมาชิก')



class LoginForm(FlaskForm):

    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
    remember_me = BooleanField(label='Remember me')







