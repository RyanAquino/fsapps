"""DTS database Model definitions."""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DTS_Table_1(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 1."""
    __tablename__ = "dts_table_1"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    account_type = Column(String(200), nullable=True)
    close_today_bal = Column(String(200), nullable=True)
    open_today_bal = Column(String(200), nullable=True)
    open_month_bal = Column(String(200), nullable=True)
    open_fiscal_year_bal = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class DTS_Table_2(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 2."""
    __tablename__ = "dts_table_2"

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
    table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class DTS_Table_3a(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 3a."""
    __tablename__ = "dts_table_3a"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    account_type = Column(String(200), nullable=True)
    security_market = Column(String(200), nullable=True)
    security_type = Column(String(200), nullable=True)
    security_type_desc = Column(String(200), nullable=True)
    transaction_today_amt = Column(String(200), nullable=True)
    transaction_mtd_amt = Column(String(200), nullable=True)
    transaction_fytd_amt = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class DTS_Table_3b(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 3b."""
    __tablename__ = "dts_table_3b"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    security_market = Column(String(200), nullable=True)
    account_type = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    adj_type = Column(String(200), nullable=True)
    adj_type_desc = Column(String(200), nullable=True)
    adj_today_amt = Column(String(200), nullable=True)
    adj_mtd_amt = Column(String(200), nullable=True)
    adj_fytd_amt = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class DTS_Table_3c(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 3c."""
    __tablename__ = "dts_table_3c"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    account_type = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    debt_catg = Column(String(200), nullable=True)
    debt_catg_desc = Column(String(200), nullable=True)
    close_today_bal = Column(String(200), nullable=True)
    open_today_bal = Column(String(200), nullable=True)
    open_month_bal = Column(String(200), nullable=True)
    open_fiscal_year_bal = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class DTS_Table_4(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 4."""
    __tablename__ = "dts_table_4"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    tax_deposit_type = Column(String(200), nullable=True)
    tax_deposit_type_desc = Column(String(200), nullable=True)
    tax_deposit_today_amt = Column(String(200), nullable=True)
    tax_deposit_mtd_amt = Column(String(200), nullable=True)
    tax_deposit_fytd_amt = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class DTS_Table_5(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 5."""
    __tablename__ = "dts_table_5"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    transaction_type_desc = Column(String(200), nullable=True)
    depositary_type_a_amt = Column(String(200), nullable=True)
    depositary_type_b_amt = Column(String(200), nullable=True)
    depositary_type_c_amt = Column(String(200), nullable=True)
    total_amt = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    tax_refund_type = Column(String(200), nullable=True)
    tax_refund_type_desc = Column(String(200), nullable=True)
    tax_refund_today_amt = Column(String(200), nullable=True)
    tax_refund_mtd_amt = Column(String(200), nullable=True)
    tax_refund_fytd_amt = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


class DTS_Table_6(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 6."""
    __tablename__ = "dts_table_6"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    transaction_type_desc = Column(String(200), nullable=True)
    depositary_type_a_amt = Column(String(200), nullable=True)
    depositary_type_b_amt = Column(String(200), nullable=True)
    depositary_type_c_amt = Column(String(200), nullable=True)
    tax_refund_type = Column(String(200), nullable=True)
    tax_refund_type_desc = Column(String(200), nullable=True)
    tax_refund_today_amt = Column(String(200), nullable=True)
    tax_refund_mtd_amt = Column(String(200), nullable=True)
    tax_refund_fytd_amt = Column(String(200), nullable=True)
    total_amt = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    table_nbr = Column(String(200), nullable=True)
    table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)


def init_db():
    """
    Initialize DB engine and tables.
    :return: DB engine
    """
    engine = create_engine("sqlite:///dts_tables.db")
    Base.metadata.create_all(engine)

    return engine
