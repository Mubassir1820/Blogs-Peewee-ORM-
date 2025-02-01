from peewee import Model, CharField, IntegerField,PrimaryKeyField, ForeignKeyField
from session import db

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = PrimaryKeyField()
    name = CharField()

class Blog(BaseModel):
    title = CharField()
    topic = CharField()
    author = ForeignKeyField(User, to_field="id")

db.connect()
db.create_tables([User])
db.close()