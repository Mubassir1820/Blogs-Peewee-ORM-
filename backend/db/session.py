from peewee import PostgresqlDatabase
from core.config import settings

db = PostgresqlDatabase(
    'blog_db',
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_SERVER,
    port=settings.POSTGRES_PORT
    )

def get_db():
    try:
        db.connect()
        yield db
    finally:
        db.close()