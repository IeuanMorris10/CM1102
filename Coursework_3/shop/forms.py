from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import  DataRequired, Length, Email, EqualTo, ValidationError, Regexp

class RegisterForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired(), Length(min = 5, max = 40)])
    username = StringField("Username", validators = [DataRequired(), Length(min = 3, max = 20)])
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Regexp('^.{5,15}$', message='Your password should be between 5 and 15 characters long.')])
    passwordConfirm = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password", message = "Passwords must match.")])
    submit = SubmitField("  Create Account  ")

    def validateUsername(self, username):
        User = User.query.filter_by(username = username.data).first()
        if User:
            raise ValidationError("Username already exists, please choose a different one.")

    def validateEmail(self, email):
        User = User.query.filter_by(email = email.data).first()
        if User:
            raise ValidationError("Email already exists, please try again.")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('  Login  ')
