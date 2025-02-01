from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'blog_db',
    user="mubassir",
    password='muba12',
    host='localhost',
    port=5435
    )

def get_db():
    try:
        db.connect()
        yield db
    finally:
        db.close()