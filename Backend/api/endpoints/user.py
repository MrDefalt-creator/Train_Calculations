from fastapi import APIRouter, Depends, Response, Request
from schemas.user import Login
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/login")
def login(data: Login, response: Response):
    access, refresh = UserService.login(data.login, data.password)

    response.set_cookie(key="refresh", value=access,
                        httponly=True, samesite="lax",
                        secure=False
                        )

    return {
        "token": access,
    }

@router.post("/refresh")
def update_token(request: Request):
    refresh = request.cookies.get("refresh")

    token = UserService.update_access_token(refresh)

    return {
        "token": token,
    }





