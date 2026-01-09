from database.database import SessionLocal
from repositories.user_repository import UserRepository
from services.user_service import UserService
from fastapi import Depends


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_service(db=Depends(get_db)):
    repo = UserRepository(db)
    return UserService(repo)
