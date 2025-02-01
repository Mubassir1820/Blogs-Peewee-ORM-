# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class User(peewee.Model):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(max_length=255)
    class Meta:
        table_name = "user"


@snapshot.append
class Blog(peewee.Model):
    title = CharField(max_length=255)
    topic = CharField(max_length=255)
    author = snapshot.ForeignKeyField(index=True, model='user')
    class Meta:
        table_name = "blog"


