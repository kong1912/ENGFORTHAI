from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length, Email
from inside import cursor, cursor_dict



class RegisterForm(FlaskForm):
    

    firstname = StringField('ชื่อจริง', validators=[DataRequired(),Length(min=2, max=45, message="ชื่อจริงต้องมีความยาว 2-45 ตัวอักษร")])
    lastname = StringField('นามสกุล', validators=[DataRequired(),Length(min=2, max=45, message="นามสกุลตเองมีความยาว 2-45 ตัวอักษร")])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('ชื่อผู้ใช้', validators=[DataRequired(),Length(min=6, max=20, message="ชื่อผู้ใช้ต้องมีความยาว 6-20 ตัวอักษร")])
    password = PasswordField('รหัสผ่าน', validators=[DataRequired(),Length(min=8, max=16, message="รหัสผ่านต้องมีความยาว 8-16 ตัวอักษร")])
    confirm_password = PasswordField('ยืนยันรหัสผ่าน', validators=[EqualTo('password',message="รหัสผ่านยืนยันไม่เหมือนกับรหัสผ่าน"), DataRequired()])
    submit = SubmitField('สมัครสมาชิก')

    def validate_username(self, username):
        cursor.execute('SELECT username FROM user WHERE username = %s', (username.data))
        data = cursor.fetchone()
        if data:
            raise ValidationError('username นี้มีอยู่ในระบบแล้ว')

    def validate_email(self, email):
        cursor.execute('SELECT email FROM user WHERE email = %s', (email.data))
        data = cursor.fetchone()
        if data:
            raise ValidationError('email นี้มีอยู่ในระบบแล้ว')
                


class LoginForm(FlaskForm):

    username = StringField('ชื่อผู้ใช้', validators=[DataRequired()])
    password = PasswordField('รหัสผ่าน', validators=[DataRequired()])
    submit = SubmitField('เข้าสู่ระบบ')


    def validate_user(self, username, password):
        cursor_dict('SELECT username and password FROM user WHERE username = %s and password = %s', (username.data, password.data))
        data = cursor_dict.fetchone()
        if data['username'] is None:
            raise ValidationError('username หรือ password ไม่ถูกต้อง')
        if data['password'] is None:
            raise ValidationError('password ไม่ถูกต้อง')











