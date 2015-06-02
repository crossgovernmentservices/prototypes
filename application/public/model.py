from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, email):
        self.email = email

    def get_id(self):
        return self.email
