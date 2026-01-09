from fastapi import APIRouter, Depends, HTTPException
from schemas.user import Login
from services.user_service import UserService
from core.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/login")
def login(data: Login, service: UserService = Depends(get_user_service)):
    user = service.login(data.login, data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid login or password")

    return {
        "id": user.id,
        "login": user.login,
        "admin": user.admin_rights
    }