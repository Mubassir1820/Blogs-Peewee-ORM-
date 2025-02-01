# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class User(peewee.Model):
    id = IntegerField()
    name = CharField(max_length=255)
    class Meta:
        table_name = "user"


