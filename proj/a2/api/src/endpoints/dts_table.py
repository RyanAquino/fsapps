from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from api.src.container import Application
from api.src.services.dts_tables_service import DTSTablesService

router = APIRouter()


@router.get("/")
@inject
def dts_table(
    table_name: str,
    dts_tables_service: DTSTablesService = Depends(
        Provide[Application.services.dts_tables_service]
    ),
):
    return dts_tables_service.get_data(table_name)
