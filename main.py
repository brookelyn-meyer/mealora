from fastapi import FastAPI
from database import get_all_groceries

app = FastAPI()


@app.get("/")
def home():
    return {"message": "MealOra API is running"}


@app.get("/groceries")
def get_groceries():
    groceries = get_all_groceries()

    return groceries