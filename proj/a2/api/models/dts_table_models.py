from sqlalchemy import Column, Integer, String

from api.database import Base


class Operating_Cash_Balance(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 1."""
    __tablename__ = "operating_cash_balance"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    account_type = Column(String(200), nullable=True)
    close_today_bal = Column(String(200), nullable=True)
    open_today_bal = Column(String(200), nullable=True)
    open_month_bal = Column(String(200), nullable=True)
    open_fiscal_year_bal = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_nm = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class Deposits_Withdrawals_Operating_Cash(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 2."""
    __tablename__ = "deposits_withdrawals_operating_cash"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    account_type = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    transaction_catg = Column(String(200), nullable=True)
    transaction_catg_desc = Column(String(200), nullable=True)
    transaction_today_amt = Column(String(200), nullable=True)
    transaction_mtd_amt = Column(String(200), nullable=True)
    transaction_fytd_amt = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_nm = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class Public_Debt_Transactions(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 3."""
    __tablename__ = "public_debt_transactions"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    security_market = Column(String(200), nullable=True)
    security_type = Column(String(200), nullable=True)
    security_type_desc = Column(String(200), nullable=True)
    transaction_today_amt = Column(String(200), nullable=True)
    transaction_mtd_amt = Column(String(200), nullable=True)
    transaction_fytd_amt = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_nm = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class Adjustment_Public_Debt_Transactions_Cash_Basis(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 4."""
    __tablename__ = "adjustment_public_debt_transactions_cash_basis"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    adj_type = Column(String(200), nullable=True)
    adj_type_desc = Column(String(200), nullable=True)
    adj_today_amt = Column(String(200), nullable=True)
    adj_mtd_amt = Column(String(200), nullable=True)
    adj_fytd_amt = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_nm = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class Debt_Subject_To_Limit(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 5."""
    __tablename__ = "debt_subject_to_limit"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    debt_catg = Column(String(200), nullable=True)
    debt_catg_desc = Column(String(200), nullable=True)
    close_today_bal = Column(String(200), nullable=True)
    open_today_bal = Column(String(200), nullable=True)
    open_month_bal = Column(String(200), nullable=True)
    open_fiscal_year_bal = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_nm = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class Inter_Agency_Tax_Transfers(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 6."""
    __tablename__ = "inter_agency_tax_transfers"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    classification = Column(String(200), nullable=True)
    today_amt = Column(String(200), nullable=True)
    mtd_amt = Column(String(200), nullable=True)
    fytd_amt = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_nm = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class Income_Tax_Refunds_Issued(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 7."""
    __tablename__ = "income_tax_refunds_issued"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    tax_refund_type = Column(String(200), nullable=True)
    tax_refund_type_desc = Column(String(200), nullable=True)
    tax_refund_today_amt = Column(String(200), nullable=True)
    tax_refund_mtd_amt = Column(String(200), nullable=True)
    tax_refund_fytd_amt = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_nm = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class Federal_Tax_Deposits(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 8."""
    __tablename__ = "federal_tax_deposits"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    tax_deposit_type = Column(String(200), nullable=True)
    tax_deposit_type_desc = Column(String(200), nullable=True)
    tax_deposit_today_amt = Column(String(200), nullable=True)
    tax_deposit_mtd_amt = Column(String(200), nullable=True)
    tax_deposit_fytd_amt = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_nm = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class Short_Term_Cash_Investments(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 9."""
    __tablename__ = "short_term_cash_investments"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    transaction_type_desc = Column(String(200), nullable=True)
    depositary_type_a_amt = Column(String(200), nullable=True)
    depositary_type_b_amt = Column(String(200), nullable=True)
    depositary_type_c_amt = Column(String(200), nullable=True)
    total_amt = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_nm = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)
