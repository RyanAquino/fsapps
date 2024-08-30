from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from api.src.container import Application
from api.src.security import get_current_user
from api.src.services.spy_finance_service import SPYFinanceService

router = APIRouter()


@router.get("/")
@inject
def spy_finance(
    _: str = Depends(get_current_user),
    spy_finance_service: SPYFinanceService = Depends(
        Provide[Application.services.spy_finance_service]
    ),
):
    return spy_finance_service.get_data()
