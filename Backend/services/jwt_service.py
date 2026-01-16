from datetime import timedelta, datetime, timezone

import jwt

from core.config import Settings

class JwtService:
    def __init__(self):
        self.settings = Settings

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else :
            expire = datetime.now(timezone.utc) + timedelta(self.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        to_encode.update({"type": "access"})
        encoded_jwt = jwt.encode(to_encode, self.settings.SECRET_KEY_ACCESS, algorithm=self.settings.ALGORITHM)
        return encoded_jwt

    def create_refresh_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(days=self.settings.REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode.update({"exp": expire})
        to_encode.update({"type": "refresh"})
        encoded_jwt = jwt.encode(to_encode, self.settings.SECRET_KEY_REFRESH, algorithm=self.settings.ALGORITHM)
        return encoded_jwt

    def decode_access_token(self, token: str):
        payload = jwt.decode(
            token,
            self.settings.SECRET_KEY_ACCESS,
            algorithms=[self.settings.ALGORITHM]
        )
        if payload.get("type") != "access":
            raise jwt.InvalidTokenError()
        return payload
    def decode_refresh_token(self, token: str):
        payload = jwt.decode(
            token,
            self.settings.SECRET_KEY_REFRESH,
            algorithms=[self.settings.ALGORITHM]
        )
        if payload.get("type") != "refresh":
            raise jwt.InvalidTokenError()
        return payload
