from typing import Union
from typing_extensions import Annotated
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from api.models.models import User
from api.crud.user_operations import UserOperations
from api.crud.dts_table_operations import DTSTableOperations
from api.user_dependencies import init_db

router = APIRouter()


@router.get("/")
def dts_table(
    table_name: Annotated[str, Query(max_length=50)],
    fiscal_year: Annotated[Union[str, None], Query(max_length=50)] = None,
    calendar_year: Annotated[Union[str, None], Query(max_length=50)] = None,
    transaction_type: Annotated[Union[str, None], Query(max_length=50)] = None,
    db: Session = Depends(init_db),
):
    """Get all data for a specific table"""
    # userOps = UserOperations(db)
    # current_user: User = userOps.get_current_active_user()
    # if current_user:
    #     dts_table_operations = DTSTableOperations(db)
    #     data = dts_table_operations.get_all_data(table_name)
    #     return data
    # return None
    dts_table_operations = DTSTableOperations(db)
    data = dts_table_operations.get_filtered_data(
        table_name,
        record_fiscal_year=fiscal_year,
        record_calendar_year=calendar_year,
        transaction_type=transaction_type,
    )
    return data
