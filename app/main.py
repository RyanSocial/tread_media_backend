import uvicorn
from fastapi import FastAPI, HTTPException
from app.crud.event_type import create_event_type, get_event_types, get_event_type, update_event_type, delete_event_type

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)


@app.post("/event_types/")
def add_event_type(name: str):
    event_type_id = create_event_type(name)
    return [{"id": row[0], "name": row[1]} for row in rows]


@app.get("/event_types/")
def read_event_types():
    return get_event_types()


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
