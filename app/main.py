import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import logging

from sqlalchemy.orm import Session

from app.crud.users import get_user
from app.db.connection import get_db
from app.schemas.user_type import User

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


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
