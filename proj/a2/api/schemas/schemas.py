from typing import Optional

from pydantic import BaseModel


class UserDBSchema(BaseModel):
    id: int
    username: str
    is_active: bool

    class Config:
        from_attributes = True
        extra = "allow"


class DTSBaseDBSchema(BaseModel):
    id: int
    record_date: str
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


class OperatingCashBalanceDBSchema(DTSBaseDBSchema):
    account_type: str
    close_today_bal: str
    open_today_bal: int
    open_month_bal: int
    open_fiscal_year_bal: int

    class Config:
        from_attributes = True
        extra = "allow"


class AdjustmentPublicDebtTransactionsCashBasisDBSchema(DTSBaseDBSchema):
    transaction_type: str
    adj_type: str
    adj_type_desc: str
    adj_today_amt: str
    adj_mtd_amt: str
    adj_fytd_amt: str

    class Config:
        from_attributes = True
        extra = "allow"
