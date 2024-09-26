from pydantic import BaseModel


class EventType(BaseModel):
    id: int
    name: str  # e.g., multi-day, gravel, ultra-marathon, etc.
