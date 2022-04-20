from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length, Email
from inside import cursor, cursor_dict




class RegisterForm(FlaskForm):
    
    firstname = StringField('ชื่อจริง', validators=[DataRequired(message="กรุณากรอกชื่อจริง"),
                                                 Length(min=2, max=45, message="ชื่อจริงต้องมีความยาว 2-45 ตัวอักษร")])
    lastname = StringField('นามสกุล', validators=[DataRequired(message="กรุณากรอกนามสกุล"),
                                                 Length(min=2, max=45, message="นามสกุลตเองมีความยาว 2-45 ตัวอักษร")])
    email = StringField('E-mail', validators=[DataRequired(message="กรุณากรอกEmail"), Email()])
    username = StringField('ชื่อผู้ใช้', validators=[DataRequired(message="กรุณากรอกชื่อผู้ใช้"),Length(min=6, max=20, 
                                                                                              message="ชื่อผู้ใช้ต้องมีความยาว 6-20 ตัวอักษร")])
    password = PasswordField('รหัสผ่าน', validators=[DataRequired(message="กรุณากรอกรหัสผ่าน"),
                                                   Length(min=4, max=16, message="รหัสผ่านต้องมีความยาว 4-16 ตัวอักษร")])
    confirm_password = PasswordField('ยืนยันรหัสผ่าน', validators=[EqualTo('password',message="รหัสผ่านยืนยันไม่เหมือนกับรหัสผ่าน"),
                                                                DataRequired(message="กรุณากรอกรหัสผ่านยืนยัน")])
    submit = SubmitField('สมัครสมาชิก')


    def validate_user(self):

        cursor_dict.execute("SELECT * FROM user")
        data = cursor.fetchall()

        errors = {}
        
        if self.username in data['username']:
            errors += flash('username นี้มีอยู่ในระบบแล้ว')
        
        if self.email in data['email']:
            errors += flash('email นี้มีอยู่ในระบบแล้ว')

        return errors

        

        




       
        
        





    

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


    def validate_user(self, username):
        cursor_dict('SELECT username, password FROM user WHERE username = %s', (username.data))
        data = cursor_dict.fetchone()
        if not data:
            raise ValidationError('username หรือ password ไม่ถูกต้อง')
        if data['password'] != self.password.data:
            raise ValidationError('password ไม่ถูกต้อง')











