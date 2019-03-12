from models.base_model import BaseModel
import peewee as pw
from playhouse.postgres_ext import ArrayField,TextField



class General(BaseModel):
    name = pw.CharField()
    contents = ArrayField(TextField, null=True) 