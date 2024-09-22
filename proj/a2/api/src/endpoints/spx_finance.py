from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from api.src.container import Application
from api.src.security import get_current_user
from api.src.services.spx_finance_service import SPXFinanceService
from api.src.services.spy_finance_service import SPYFinanceService

router = APIRouter()


@router.get("/options")
@inject
def finance_opts(
    _: str = Depends(get_current_user),
    spx_finance_service: SPXFinanceService = Depends(
        Provide[Application.services.spx_finance_service]
    ),
):
    return spx_finance_service.get_options_data()
