from models.base_model import BaseModel
import peewee as pw
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

class User(BaseModel, UserMixin):
    username = pw.CharField(unique=True)
    email = pw.CharField(unique=True)
    password = pw.CharField(unique=False)
    preference = pw.TextField

    def validate(self):
        duplicate_username = User.get_or_none(User.username == self.username)
        duplicate_email = User.get_or_none(User.email == self.email)
        if duplicate_username and duplicate_username.id != self.id:
            self.errors.append('Username not unique')
        if duplicate_email and duplicate_email.id != self.id :
            self.errors.append('Email not unique')
        if len(self.password) < 8 or len(self.password) > 25:
            self.errors.append('Password must between 8-25 characters.')
        else:
            self.password=generate_password_hash(self.password)
