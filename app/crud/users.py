from sqlalchemy.orm import Session
from app.models.user_model import UserModel
from app.schemas.user_type import UserCreate, UserUpdate


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def create_user(db: Session, user: UserCreate):
    db_user = UserModel(
        username=user.username,
        full_name=user.full_name,
        google_id=user.google_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Add more CRUD operations as needed
