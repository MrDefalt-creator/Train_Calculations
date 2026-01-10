from fastapi import APIRouter, Depends, Response
from schemas.user import Login
from services.user_service import UserService
from core.dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/login")
def login(data: Login, response: Response, service: UserService = Depends(get_user_service)):
    access, refresh = service.login(data.login, data.password)

    response.set_cookie(key="refresh", value=access,
                        httponly=True, samesite="lax",
                        secure=False
                        )

    return {
        "token": access,
    }