#main.py
from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

@app.get("/")
def hello_api():
    print(settings.DATABASE_URL)
    return {"msg":"Hello FastAPI"}