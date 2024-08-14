from fastapi import APIRouter

from api.endpoints import auth, dts_table

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth")
api_router.include_router(dts_table.router, prefix="/dts-tables")
