from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class TestForm(FlaskForm):
    test = StringField(label='test')