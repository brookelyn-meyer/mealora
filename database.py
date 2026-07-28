import os

import psycopg
from dotenv import load_dotenv


load_dotenv()


def get_database_connection():
    return psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )


def add_grocery_to_database(name, quantity, location, expiration_date):
    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO groceries (name, quantity, location, expiration_date)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
        """,
        (name, quantity, location, expiration_date),
    )

    grocery_id = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return grocery_id


def get_all_groceries():
    connection = get_database_connection()
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


def delete_grocery_from_database(grocery_id):
    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM groceries
        WHERE id = %s
        """,
        (grocery_id,),
    )

    connection.commit()

    deleted_rows = cursor.rowcount

    cursor.close()
    connection.close()

    return deleted_rows

def update_grocery_in_database(
    grocery_id,
    name,
    quantity,
    location,
    expiration_date,
):
    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE groceries
        SET name = %s,
            quantity = %s,
            location = %s,
            expiration_date = %s
        WHERE id = %s
        """,
        (
            name,
            quantity,
            location,
            expiration_date,
            grocery_id,
        ),
    )

    connection.commit()

    updated_rows = cursor.rowcount

    cursor.close()
    connection.close()

    return updated_rows