import jwt
from fastapi import Depends, HTTPException, Request
from database.database import SessionLocal
from repositories.user_repository import UserRepository
from services.jwt_service import JwtService
from services.user_service import UserService
from core.config import settings, Settings
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

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


def get_jwt_payload(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    jwt_service: JwtService = Depends(get_jwt_service),
):
    token = credentials.credentials

    if not token:
        raise HTTPException(status_code=401, detail="Token missing")

    try:
        payload = jwt_service.decode_access_token(token)
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_refresh_payload(
    request: Request,
    jwt_service: JwtService = Depends(get_jwt_service),
):
    token = request.cookies.get("refresh")

    if not token:
        raise HTTPException(status_code=401, detail="Token missing")

    try:
        payload = jwt_service.decode_refresh_token(token)

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token")

        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")