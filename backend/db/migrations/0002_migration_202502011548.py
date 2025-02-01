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


def forward(old_orm, new_orm):
    old_user = old_orm['user']
    user = new_orm['user']
    return [
        # Convert datatype of the field user.id: INT -> AUTO,
        user.update({user.id: old_user.id.cast('INTEGER')}).where(old_user.id.is_null(False)),
    ]


def backward(old_orm, new_orm):
    old_user = old_orm['user']
    user = new_orm['user']
    return [
        # Convert datatype of the field user.id: AUTO -> INT,
        user.update({user.id: old_user.id.cast('INTEGER')}).where(old_user.id.is_null(False)),
    ]
