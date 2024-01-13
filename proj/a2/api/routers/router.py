from fastapi import APIRouter

from api.routers import user_token

api_router = APIRouter()

api_router.include_router(user_token.router, prefix="/auth")
