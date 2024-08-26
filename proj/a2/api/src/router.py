from fastapi import APIRouter

from api.src.endpoints import aaii_sentiment, auth, dts_table

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth")
api_router.include_router(dts_table.router, prefix="/dts-tables")
api_router.include_router(aaii_sentiment.router, prefix="/sentiment-survey")
