from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):

    #DataRequired - user must give input
    #Length- minimum and maximum length of the username
    username = StringField('Username', validators = [DataRequired(),
                                                     Length(min = 2, max = 20) ])
    #Treat email as email with Email()
    email = StringField('Email', validators = [DataRequired(),
                                               Email()]  )

    #Treat possword varaible as password with PasswordField
    password = PasswordField('Password', validators = [DataRequired()])
    #Validate password by comparing with EqualTo validator
    confirm_password = PasswordField('Confirm Password',validators = [DataRequired(),
                                                                      EqualTo('password')] )
    #Submit data
    submit = SubmitField('Sign up')

    #validate username doesn't exist yet
    def validate_username(self, username):

        user = User.query.filter_by(user_name = username.data).first()
        if user.user_name:
            raise ValidationError(f'User name {user.user_name} already exists')

    #validate email doesn't exist yet in the system
    def validate_email(self, email):

        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError(f'Email {user.email} already exists')

class LoginForm(FlaskForm):

    #DataRequired - user must give input
    #Length- minimum and maximum length of the username
    #Login into site with username and password
    email = StringField('Email', validators=[DataRequired(),
                                             Email()])

    #Treat possword varaible as password with PasswordField
    password = PasswordField('Password', validators = [DataRequired()])
    #Submit data
    remember = BooleanField('Remember Me') #Secure cookie boolean field
    submit = SubmitField('Login')