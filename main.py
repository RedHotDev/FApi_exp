from fastapi import FastAPI
from config import setting
from routes import category
from database import create_table

app = FastAPI(title=setting.app_name)

app.include_router(category.routerCategory)



# create_table()

@app.get("/")
def read_root():
    return {"Hello": "World"}

