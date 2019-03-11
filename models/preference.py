from models.base_model import BaseModel
import peewee as pw
from playhouse.postgres_ext import ArrayField,TextField



class Preference(BaseModel):
    categories = pw.CharField()
    articles = ArrayField(TextField, null=True)