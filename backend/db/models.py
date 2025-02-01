from peewee import Model, CharField, IntegerField
from session import db

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = IntegerField()
    name = CharField()

db.connect()
db.create_tables([User])
db.close()