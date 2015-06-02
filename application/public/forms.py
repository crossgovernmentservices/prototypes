from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Email
from application.services.people import People
from .model import User


people = People()

class LoginForm(Form):
    """A login form which only cares about the presence of a
    valid email address.
    Set the email, and create the user's profile.
    Yes - the login form creates the user's profile.
    This is only bells & whistles, after all.

    """

    email = TextField('Email', validators=[DataRequired(), Email()])

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        email = self.email.data
        self.user = User(email)

        people.create_user(email)
        if not people.read_profile(email):
            people.create_default_profile(email)

        return True
