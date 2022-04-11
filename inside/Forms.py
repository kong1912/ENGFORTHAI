from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


#create register form
class RegisterForm(FlaskForm):
    fullname = StringField(Label='Full Name', validators=[DataRequired()])
    username = StringField(Label='Username', validators=[DataRequired()])
    password = PasswordField(Label='Password', validators=[DataRequired()])
    submit = SubmitField(Label='Register')



class LoginForm(FlaskForm):

    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')







