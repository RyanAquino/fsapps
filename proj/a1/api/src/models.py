"""DTS database Model definitions."""

import os

from dotenv import load_dotenv
from sqlalchemy import Column, Float, Integer, String, create_engine, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


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


class AAIISentiment(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """AAI Sentiment model table."""
    __tablename__ = "aaii_sentiment"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    bullish = Column(Float(), nullable=True)
    neutral = Column(Float(), nullable=True)
    bearish = Column(Float(), nullable=True)
    total = Column(Float(), nullable=True)
    bullish_eight_week_mov_avg = Column(Float(), nullable=True)
    bull_bear_spread = Column(Float(), nullable=True)
    bullish_avg = Column(Float(), nullable=True)
    bull_pos_avg_std_dev = Column(Float(), nullable=True)
    bull_neg_avg_std_dev = Column(Float(), nullable=True)
    s_and_p_weekly_high = Column(Float(), nullable=True)
    s_and_p_weekly_low = Column(Float(), nullable=True)
    s_and_p_weekly_close = Column(Float(), nullable=True)


class SPYFinance(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 1."""
    __tablename__ = "spy_finance"

    id = Column(Integer, primary_key=True)
    record_date = Column(DateTime(), nullable=True)
    open = Column(Float(), nullable=True)
    high = Column(Float(), nullable=True)
    low = Column(Float(), nullable=True)
    close = Column(Float(), nullable=True)
    adj_close = Column(Float(), nullable=True)
    volume = Column(Integer(), nullable=True)


def init_db():
    """
    Initialize DB engine and tables.
    :return: DB engine
    """
    load_dotenv()
    # Returns `default_value` if the key doesn't exist
    proj = os.environ.get("working_env", "local")
    conn = str(os.getenv("conn"))
    if proj == "remote":
        with open("/run/secrets/db_conn") as f:
            conn = f.readlines()[0]

    engine = create_engine(conn, pool_recycle=300, pool_pre_ping=True)
    # disable for prod, user has only select and insert privileges
    Base.metadata.create_all(engine)

    return engine
