from fastapi import APIRouter, Query, Depends

from api.container import Application
from api.services.dts_tables_service import DTSTablesService
from dependency_injector.wiring import Provide, inject
router = APIRouter()


@router.get("/")
@inject
def dts_table(
    table_name: str,
    dts_tables_service: DTSTablesService = Depends(Provide[Application.services.dts_tables_service]),
):
    return dts_tables_service.get_data(table_name)
