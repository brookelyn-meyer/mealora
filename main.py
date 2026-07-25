from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import get_all_groceries

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