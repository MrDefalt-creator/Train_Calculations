from fastapi import APIRouter

from schemas.user import Login

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/login")
async def login(data: Login):
    return data
