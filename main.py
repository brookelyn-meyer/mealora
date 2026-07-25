from fastapi import FastAPI
from database import get_all_groceries

app = FastAPI()


@app.get("/groceries")
def get_groceries():
    groceries = get_all_groceries()

    return [
        {
            "id": grocery[0],
            "name": grocery[1],
            "quantity": grocery[2],
            "location": grocery[3],
            "expiration_date": grocery[4]
        }
        for grocery in groceries
    ]