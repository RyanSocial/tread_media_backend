from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    username: str
    full_name: str
    google_id: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
