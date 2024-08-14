from typing import Optional

from pydantic import BaseModel


class UserDBSchema(BaseModel):
    id: int
    username: str
    is_active: bool

    class Config:
        from_attributes = True
        extra = "allow"


class OperatingCashBalanceDBSchema(BaseModel):
    id: int
    record_date: str
    account_type: str
    close_today_bal: str
    open_today_bal: int
    open_month_bal: int
    open_fiscal_year_bal: int
    table_nbr: str
    table_nm: str
    sub_table_name: str
    src_line_nbr: str
    record_fiscal_year: int
    record_fiscal_quarter: int
    record_calendar_year: int
    record_calendar_quarter: int
    record_calendar_month: int
    record_calendar_day: int

    class Config:
        from_attributes = True
