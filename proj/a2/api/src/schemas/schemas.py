import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


class UserDBSchema(BaseModel):
    id: int
    username: str
    is_active: bool

    class Config:
        from_attributes = True
        extra = "allow"


class DTSBaseDBSchema(BaseModel):
    id: int
    record_date: Optional[str] = None
    table_nbr: Optional[str] = None
    table_nm: Optional[str] = None
    sub_table_name: Optional[str] = None
    src_line_nbr: Optional[str] = None
    record_fiscal_year: Optional[int] = None
    record_fiscal_quarter: Optional[int] = None
    record_calendar_year: Optional[int] = None
    record_calendar_quarter: Optional[int] = None
    record_calendar_month: Optional[int] = None
    record_calendar_day: Optional[int] = None

    class Config:
        from_attributes = True
        extra = "allow"


class OperatingCashBalanceDBSchema(DTSBaseDBSchema):
    account_type: str
    close_today_bal: str
    open_today_bal: int
    open_month_bal: int
    open_fiscal_year_bal: int


class AdjustmentPublicDebtTransactionsCashBasisDBSchema(DTSBaseDBSchema):
    transaction_type: str
    adj_type: str
    adj_type_desc: str
    adj_today_amt: str
    adj_mtd_amt: str
    adj_fytd_amt: str


class DebtSubjectToLimitDBSchema(DTSBaseDBSchema):
    debt_catg: str
    debt_catg_desc: str
    close_today_bal: str
    open_today_bal: str
    open_month_bal: str
    open_fiscal_year_bal: str


class DepositsWithdrawalsOperatingCashDBSchema(DTSBaseDBSchema):
    account_type: Optional[str] = None
    transaction_type: Optional[str] = None
    transaction_catg: Optional[str] = None
    transaction_catg_desc: Optional[str] = None
    transaction_today_amt: Optional[str] = None
    transaction_mtd_amt: Optional[str] = None
    transaction_fytd_amt: Optional[str] = None


class FederalTaxDepositsDBSchema(DTSBaseDBSchema):
    tax_deposit_type: str
    tax_deposit_type_desc: str
    tax_deposit_today_amt: str
    tax_deposit_mtd_amt: str
    tax_deposit_fytd_amt: str


class IncomeTaxRefundsIssuedDBSchema(DTSBaseDBSchema):
    tax_refund_type: str
    tax_refund_type_desc: str
    tax_refund_today_amt: str
    tax_refund_mtd_amt: str
    tax_refund_fytd_amt: str


class InterAgencyTaxTransfersDBSchema(DTSBaseDBSchema):
    classification: str
    today_amt: str
    mtd_amt: str
    fytd_amt: str


class PublicDebtTransactionsDBSchema(DTSBaseDBSchema):
    transaction_type: str
    security_market: str
    security_type: str
    security_type_desc: str
    transaction_today_amt: str
    transaction_mtd_amt: str
    transaction_fytd_amt: str


class ShortTermCashInvestmentsDBSchema(DTSBaseDBSchema):
    transaction_type: str
    transaction_type_desc: str
    depositary_type_a_amt: str
    depositary_type_b_amt: str
    depositary_type_c_amt: str
    total_amt: str


class AAIISentimentDBSchema(BaseModel):
    id: int
    record_date: Optional[datetime.datetime] = None
    bullish: Optional[float] = None
    neutral: Optional[float] = None
    bearish: Optional[float] = None
    total: Optional[float] = None
    bullish_eight_week_mov_avg: Optional[float] = None
    bull_bear_spread: Optional[float] = None
    bullish_avg: Optional[float] = None
    bull_pos_avg_std_dev: Optional[float] = None
    bull_neg_avg_std_dev: Optional[float] = None
    s_and_p_weekly_high: Optional[float] = None
    s_and_p_weekly_low: Optional[float] = None
    s_and_p_weekly_close: Optional[float] = None

    class Config:
        from_attributes = True

    @field_validator("bullish", "neutral", "bearish", "total")
    def round_values(cls, v):
        return round(v, 2)
