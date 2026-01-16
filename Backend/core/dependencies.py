from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError


from services.jwt_service import JwtService
from core.config import Settings


settings = Settings()

jwt_service = JwtService()

oauth2_scheme = OAuth2PasswordBearer("/users/login")

def validate_access_token(access_token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt_service.decode_access_token(access_token)
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token"
        )
    return payload["sub"]


