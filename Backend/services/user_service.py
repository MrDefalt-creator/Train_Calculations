from pwdlib import PasswordHash
from fastapi import HTTPException
from repositories.user_repository import UserRepository
from services.jwt_service import JwtService


class UserService:
    def __init__(self, user_repository: UserRepository, jwt_service: JwtService):
        self.user_repository = user_repository
        self.jwt_service = jwt_service
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