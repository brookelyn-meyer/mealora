from datetime import date

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from database import (
    add_grocery_to_database,
    get_all_groceries,
    delete_grocery_from_database,
    update_grocery_in_database,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GroceryCreate(BaseModel):
    name: str
    quantity: str
    location: str
    expiration_date: date | None = None


@app.get("/")
def home():
    return {"message": "MealOra API is running"}


@app.get("/groceries")
def get_groceries():
    groceries = get_all_groceries()

    return [
        {
            "id": grocery[0],
            "name": grocery[1],
            "quantity": grocery[2],
            "location": grocery[3],
            "expiration_date": grocery[4],
        }
        for grocery in groceries
    ]


@app.post("/groceries")
def create_grocery(grocery: GroceryCreate):
    grocery_id = add_grocery_to_database(
        grocery.name,
        grocery.quantity,
        grocery.location,
        grocery.expiration_date,
    )

    return {
        "id": grocery_id,
        "name": grocery.name,
        "quantity": grocery.quantity,
        "location": grocery.location,
        "expiration_date": grocery.expiration_date,
    }

@app.put("/groceries/{grocery_id}")
def update_grocery(grocery_id: int, grocery: GroceryCreate):
    updated_rows = update_grocery_in_database(
        grocery_id,
        grocery.name,
        grocery.quantity,
        grocery.location,
        grocery.expiration_date,
    )

    if updated_rows == 0:
        raise HTTPException(status_code=404, detail="Grocery not found")

    return {
        "id": grocery_id,
        "name": grocery.name,
        "quantity": grocery.quantity,
        "location": grocery.location,
        "expiration_date": grocery.expiration_date,
    }

@app.delete("/groceries/{grocery_id}")
def delete_grocery(grocery_id: int):
    deleted_rows = delete_grocery_from_database(grocery_id)

    if deleted_rows == 0:
        raise HTTPException(status_code=404, detail="Grocery not found")

    return {"message": "Grocery deleted"}