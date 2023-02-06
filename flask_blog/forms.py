from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_blog.models import Users


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    '''
    For anyone wondering how validate_username() and validate_email() are being called, 
    these functions are called with the FlaskForm class that our RegistrationForm class
    inherited from. If you look at the definition for validate_on_submit(), and from there, 
    the definition for validate(), that validate function contains the following line:

    inline = getattr(self.__class__, 'validate_%s' % name, None)

    There is a lot going on in the background, but from what I can tell, Flask is checking
    for extra functions created with the naming pattern: "validate_(field name)", and later
    calling those extra functions. Correct me if I'm wrong
    '''

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        raise ValidationError("That Username is taken please choose a different one.")


    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That Email is taken please choose a different one.")


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')    

