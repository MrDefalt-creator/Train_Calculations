
from fastapi import Depends
from database.database import SessionLocal
from repositories.user_repository import UserRepository
from services.jwt_service import JwtService
from services.user_service import UserService
from core.config import settings, Settings


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_settings() -> Settings:
    return settings


def get_jwt_service(settings: Settings = Depends(get_settings)):
    return JwtService(settings)


def get_user_service(
    db = Depends(get_db),
    jwt = Depends(get_jwt_service),
):
    repo = UserRepository(db)
    return UserService(repo, jwt)