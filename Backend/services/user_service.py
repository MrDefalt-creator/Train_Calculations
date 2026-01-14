from pwdlib import PasswordHash
from fastapi import HTTPException

from core.config import Settings
from repositories.user_repository import UserRepository
from services.jwt_service import JwtService
from database.database import SessionLocal
from sqlalchemy.orm import Session

class UserService:
    def __init__(self, db_session: Session = None, jwt_service: JwtService = None):
        self.db = db_session if db_session else SessionLocal()
        self.settings = Settings()
        self.user_repository = UserRepository(self.db)
        self.jwt_service = jwt_service or JwtService(settings=self.settings)
        self.password_hasher = PasswordHash.recommended()

    def login(self, login: str, password: str):
        user = self.user_repository.find_by_login(login)

        if not user:
            raise HTTPException(status_code=401, detail="Incorrect login or password")

        if not self.password_hasher.verify(password, user.password):
            raise HTTPException(status_code=401, detail="Incorrect login or password")

        token = self.jwt_service.create_access_token(
            data={"id": user.id, "sub": user.login, "admin": user.admin_rights}
        )

        refresh = self.jwt_service.create_refresh_token(data={"id": user.id})

        return token, refresh

    def update_access_token(self, refresh: str):
        token = self.jwt_service.decode_access_token(refresh)

        user = self.user_repository.find_by_id(token["id"])

        if not user:
            raise HTTPException(status_code=401, detail="Incorrect login or password")

        token = self.jwt_service.create_access_token(
            data={"id": user.id, "sub": user.login, "admin": user.admin_rights}
        )

        return token




