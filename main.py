from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config import setting
from routes import category, auth
from database import create_table
from schemas.schema import User, UserCreate
from database import get_db

app = FastAPI(title=setting.app_name)

app.include_router(category.routerCategory)
app.include_router(auth.routerAuth)


# create_table()

@app.get("/")
def read_root():
    return {"Hello": "World"}


