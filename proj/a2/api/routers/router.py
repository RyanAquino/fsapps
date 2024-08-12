from fastapi import APIRouter

from api.routers import user_token, dts_table

api_router = APIRouter()

api_router.include_router(user_token.router, prefix="/auth")
api_router.include_router(dts_table.router, prefix="/dts_tables")
