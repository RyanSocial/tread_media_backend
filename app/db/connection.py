import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DBNAME"),
            # TODO which is this using pc NAME?
            user="postgres",
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOST"),
            port=os.getenv("PORT")
        )
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None


def test_connection():
    conn = get_connection()
    if conn:
        print("Connection successful")
        conn.close()
    else:
        print("Connection failed")


test_connection()

