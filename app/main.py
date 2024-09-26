import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.db.connection import connect, close  # Your connection logic here
from app.models.models import EventType  # Your EventType model

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:4200",  # Frontend URL, adjust as needed
    "http://127.0.0.1:4200",
    "*",  # Allow all origins, use with caution
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


@app.get("/")
def read_root():
    return {"message": "tread media backend"}


@app.get("/event-types/", response_model=list[EventType])
def read_event_types():
    """Get all event types."""
    connection, cursor = connect()
    try:
        cursor.execute("SELECT * FROM event_types;")
        event_types = cursor.fetchall()

        if not event_types:
            raise HTTPException(status_code=404, detail="No event types found.")

        # Transform the result to match the EventType model
        event_types_list = [EventType(id=et[0], name=et[1]) for et in event_types]
        return event_types_list

    except Exception as e:
        logger.error(f"An error occurred while retrieving event types: {str(e)}")
        raise HTTPException(status_code=500, detail="An internal server error occurred.")

    finally:
        close(connection, cursor)  # Ensure the connection is closed


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
