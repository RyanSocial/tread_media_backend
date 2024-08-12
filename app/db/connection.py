import psycopg2


def get_connection():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="mysecretpassword",
        host="localhost",
        port="5432"
    )
    return conn


def test_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="mysecretpassword",
            host="localhost",
            port="5432"
        )
        print("Connection successful")
        conn.close()
    except Exception as e:
        print(f"Error: {e}")


test_connection()
