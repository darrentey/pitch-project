from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username:', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email:',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password:',
                            validators=[DataRequired(),Length(min=8)])
    submit_reg = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email:',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password:',
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit_log = SubmitField('Login')


# class UpdateForm(FlaskForm):
#     username = StringField('Username:', 
#                             validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email:',
#                             validators=[DataRequired(), Email()])
#     submit = SubmitField('Update Information')