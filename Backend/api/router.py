from fastapi import APIRouter

from .endpoints import user

main_router = APIRouter()

main_router.include_router(user.router)