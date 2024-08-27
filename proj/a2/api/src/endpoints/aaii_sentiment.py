from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from api.src.container import Application
from api.src.security import get_current_user
from api.src.services.aaii_sentiment_service import AAIISentimentService

router = APIRouter()


@router.get("/")
@inject
def dts_table(
    _: str = Depends(get_current_user),
    aaii_sentiment_service: AAIISentimentService = Depends(
        Provide[Application.services.aaii_sentiment_service]
    ),
):
    return aaii_sentiment_service.get_data()
