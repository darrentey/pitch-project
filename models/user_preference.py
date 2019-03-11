from models.base_model import BaseModel
import peewee as pw
from models.user import User
from models.preference import Preference


class User_Preference(BaseModel):
    user = pw.ForeignKeyField(User, backref='preferences')
    preference = pw.ForeignKeyField(Preference, backref='users') 