import os
import psycopg
from dotenv import load_dotenv
load_dotenv()


def add_grocery_to_database(name, quantity, location, expiration_date):
    connection = psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO groceries (name, quantity, location, expiration_date)
        VALUES (%s, %s, %s, %s)
        """,
        (name, quantity, location, expiration_date)
    )

    connection.commit()

    cursor.close()
    connection.close()

    print(f"{name} was saved to the database!")




def get_all_groceries():
    connection = psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, quantity, location, expiration_date
        FROM groceries
        ORDER BY id
        """
    )

    groceries = cursor.fetchall()

    cursor.close()
    connection.close()

    return groceries