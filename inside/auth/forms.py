from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired
from inside import cursor



class RegisterForm(FlaskForm):
    

    firstname = StringField('ชื่อจริง', validators=[DataRequired()])
    lastname = StringField('นามสกุล', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), validators.Email()])
    username = StringField('ชื่อผู้ใช้', validators=[DataRequired()])
    password = PasswordField('รหัสผ่าน', validators=[DataRequired()])
    submit = SubmitField('สมัครสมาชิก')

    def validate_username(self,field):
        cursor.execute('SELECT username FROM user WHERE username = %s',(field.data))
        data = cursor.fetchone()
        if data:
            raise ValidationError('ขออภัย ชื่อผู้ใช้นี้มีอยู่แล้ว โปรดใช้ชื่ออื่น')

    def validate_email(self,field):
        cursor.execute('SELECT email FROM user WHERE email = %s',(field.data))
        data = cursor.fetchone()
        if data:
            raise ValidationError('ขออภัย email นี้มีอยู่แล้ว โปรดใช้ email อื่น')


class LoginForm(FlaskForm):

    username = StringField('ชื่อผู้ใช้', validators=[DataRequired()])
    password = PasswordField('รหัสผ่าน', validators=[DataRequired()])
    submit = SubmitField('เข้าสู่ระบบ')
    remember = BooleanField('จดจำฉัน')








