import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app import mysql
from flask_login import current_user


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        if re.match("^[a-zA-Z0-9_]+$", username.data) == None:
            raise ValidationError('username has invalid charactor!')
        user = mysql.One("user", {"username": "'%s'" % username.data}, ["id"])
        if user != 0:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = mysql.One("user", {"email":  "'%s'" % email.data}, ["id"])
        if user != 0:
            raise ValidationError('Please use a different email address.')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    note = StringField('About me', validators=[])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if re.match("^[a-zA-Z0-9_]+$", username.data) == None:
            raise ValidationError('username has invalid charactor!')

        if username.data == current_user.username:
            pass
        else:
            user = mysql.One(
                "user", {"username": "'%s'" % username.data}, ["id"])
            if user != 0:
                raise ValidationError('Please use a different username.')

    def validate_note(self, note):
        if re.match("^[a-zA-Z0-9_\'\(\) \.\_\*\`\-\@\=\+\>\<]*$", note.data) == None:
            raise ValidationError("Don't input invalid charactors!")


class PostForm(FlaskForm):
    post = StringField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')
