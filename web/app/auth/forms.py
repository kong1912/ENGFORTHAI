import re
from flask import flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from app import cursor, cursor_dict

class RegisterForm(FlaskForm):
    
    firstname = StringField('firstname', validators=[DataRequired(message="Please enter your firstname"),
                                                Length(min=2, max=45, message="Firstname must be between 2 and 45 characters long")])
    lastname = StringField('lastname', validators=[DataRequired(message="Please enter your lastname"),
                                                Length(min=2, max=45, message="Lastname must be between 2 and 45 characters long")] )
    username = StringField('username', validators=[DataRequired(message="Please enter your username"),
                                                Length(min=6, max=20, message="Username must be between 6 and 20 characters long")])
    password = PasswordField('password', validators=[DataRequired(message="Please enter your password"),
                                                    Length(min=4, max=16, message="Password must be between 4 and 16 characters long")])
    confirm_password = PasswordField('confirm password', validators=[EqualTo('password',message="Passwords must match"),
                                                            DataRequired(message="Please enter your confirm-password")])
    submit = SubmitField('Sign in')
    def validateName(self,firstname):
        if not re.match(r'^[a-zA-Z]+$', firstname.data):
            raise ValidationError('Please enter your name in English.')
    def validateSurname(self,lastname):
        if not re.match(r'^[a-zA-Z]+$', lastname.data):
            raise ValidationError('Please enter your name in English.')
    def validate_username(self,username):
        cursor.execute(f"SELECT username FROM user WHERE username = %s", (username.data))
        data = cursor.fetchone()
        if data:
            raise ValidationError(f'There is a username "{data[0]}" in the system.')

class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(message="Please enter your username")])
    password = PasswordField('Password', validators=[DataRequired(message="Please enter your password")])
    submit = SubmitField('Login')

    def validate_username(self,username):
        cursor.execute("SELECT username FROM user WHERE username = %s", (username.data))
        data = cursor.fetchone()
        if not data:
            raise ValidationError('ชื่อผู้ใช้ไม่ถูกต้อง')

    def validate_password(self,password):
        cursor.execute("SELECT password FROM user WHERE username = %s and password = %s", (self.username.data,password.data))
        data = cursor.fetchone()
        if not data:
            raise ValidationError('รหัสผ่านไม่ถูกต้อง')

class submitForm(FlaskForm):
    submit = SubmitField('Submit')
        