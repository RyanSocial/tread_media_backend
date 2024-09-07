import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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


@app.get("/")
def read_root():
    return {"message": "tread media backend"}



