import psycopg2
from dotenv import load_dotenv  # Import the load_dotenv function
import os

load_dotenv()

# Fetch the database configuration from environment variables or define them here
DATABASE_URL = f"postgresql://postgres:{os.getenv('PASSWORD')}@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DBNAME')}"


def connect():
    """Connect to the PostgreSQL database."""
    try:
        # Connect to the database
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()

        # Print the connection properties
        print("Connected to the database!")

        return connection, cursor

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


def close(connection, cursor):
    """Close the database connection."""
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Connection closed.")


connect()
