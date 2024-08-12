import psycopg2
from psycopg2 import sql


def get_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="mysecretpassword",
        host="localhost",
        port="5432"
    )


def get_event_types():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM event_types;")
            rows = cur.fetchall()
            # Convert rows to list of dictionaries
            return [{"id": row[0], "name": row[1]} for row in rows]


def get_event_type(event_type_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM event_types WHERE id = %s;", (event_type_id,))
            row = cur.fetchone()
            if row:
                return {"id": row[0], "name": row[1]}
            return None


def create_event_type(name: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO event_types (name) VALUES (%s) RETURNING id;", (name,))
            event_type_id = cur.fetchone()[0]
            conn.commit()
            return event_type_id


def update_event_type(event_type_id: int, name: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE event_types SET name = %s WHERE id = %s;", (name, event_type_id))
            conn.commit()
            return cur.rowcount > 0


def delete_event_type(event_type_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM event_types WHERE id = %s;", (event_type_id,))
            conn.commit()
            return cur.rowcount > 0
