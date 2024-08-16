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
    sub_table_name: Optional[str] = None
    src_line_nbr: str
    record_fiscal_year: int
    record_fiscal_quarter: int
    record_calendar_year: int
    record_calendar_quarter: int
    record_calendar_month: int
    record_calendar_day: int

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
    account_type: str
    transaction_type: str
    transaction_catg: str
    transaction_catg_desc: str
    transaction_today_amt: str
    transaction_mtd_amt: str
    transaction_fytd_amt: str


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
