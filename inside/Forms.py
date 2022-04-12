from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from inside import cursor



class RegisterForm(FlaskForm):
    def check_username(self, username):
        cursor.execute('SELECT username FROM user WHERE username = %s', username)
        data = cursor.fetchone()
        if data:
            raise validators.ValidationError('ขออภัย ชื่อผู้ใช้นี้มีอยู่แล้ว โปรดใช้ชื่ออื่น')

    def check_email(self, email):
        cursor.execute('SELECT email FROM user WHERE email = %s', email)
        data = cursor.fetchone()
        if data:
            raise validators.ValidationError('ขออภัย email นี้มีอยู่แล้ว โปรดใช้ email อื่น')
        

    
    firstname = StringField(Label='ชื่อจริง', validators=[DataRequired()])
    lastname = StringField(Label='นามสกุล', validators=[DataRequired()])
    username = StringField(Label='ชื่อผู้ใช้', validators=[DataRequired()])
    password = PasswordField(Label='รหัสผ่าน', validators=[DataRequired()])
    submit = SubmitField(Label='สมัครสมาชิก')



class LoginForm(FlaskForm):

    username = StringField(label='ชื่อผู้ใช้', validators=[DataRequired()])
    password = PasswordField(label='รหัสผ่าน', validators=[DataRequired()])
    submit = SubmitField(label='เข้าสู่ระบบ')
    remember_me = BooleanField(label='จดจำฉัน')







