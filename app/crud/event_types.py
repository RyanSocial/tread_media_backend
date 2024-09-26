from typing import List
from app.db.connection import connect, close  # Adjusted import statement for connection
from app.models.models import EventType  # Adjusted import statement for the EventType model


def get_all_event_types() -> List[EventType]:
    connection, cursor = connect()
    if not connection or not cursor:
        return []
    try:
        cursor.execute("SELECT id, name FROM event_types;")
        rows = cursor.fetchall()
        event_types = [EventType(id=row[0], name=row[1]) for row in rows]
        return event_types
    except Exception as e:
        print(f"An error occurred while fetching event types: {e}")
        return []
    finally:
        close(connection, cursor)


# For testing the function
if __name__ == "__main__":
    event_types = get_all_event_types()
    print(event_types)

