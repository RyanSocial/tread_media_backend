import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.crud.event_type import create_event_type, get_event_types, get_event_type, update_event_type, delete_event_type
import logging

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


@app.post("/event_types/")
def add_event_type(name: str):
    event_type_id = create_event_type(name)
    return [{"id": row[0], "name": row[1]} for row in rows]


@app.get("/event_types/")
def read_event_types():
    try:
        event_types = get_event_types()  # Use the renamed function
        if not event_types:  # Check if the list is empty
            raise HTTPException(status_code=404, detail="No Events found")
        return event_types
    except Exception as e:
        logger.error(f"Error in endpoint /event_types: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/event_types/{event_type_id}")
def read_event_type(event_type_id: int):
    event_type = get_event_type(event_type_id)
    if event_type is None:
        raise HTTPException(status_code=404, detail="EventType not found")
    return event_type


@app.put("/event_types/{event_type_id}")
def modify_event_type(event_type_id: int, name: str):
    success = update_event_type(event_type_id, name)
    if not success:
        raise HTTPException(status_code=404, detail="EventType not found")
    return {"status": "updated"}


@app.delete("/event_types/{event_type_id}")
def remove_event_type(event_type_id: int):
    success = delete_event_type(event_type_id)
    if not success:
        raise HTTPException(status_code=404, detail="EventType not found")
    return {"status": "deleted"}
