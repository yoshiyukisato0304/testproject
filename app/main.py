from fastapi import FastAPI
from router import router 
from fastapi.staticfiles import StaticFiles
from database import create_db_and_tables


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
