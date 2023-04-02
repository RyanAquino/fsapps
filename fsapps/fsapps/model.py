from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.orm import Session, relationship, declarative_base
from sqlalchemy.exc import IntegrityError

engine = create_engine("mysql+pymysql://root:@localhost/dts_tables",echo = False)

Base = declarative_base()


class TableDef(Base):
    __tablename__ = "tabledef"

    id = Column(Integer, primary_key=True)
    table_name = Column(String(200))
    table_nbr = Column(String(10))

class OpCashBal(Base):
    __tablename__ = "opcashbal"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    account_type = Column(String(200), nullable=True)
    close_today_bal = Column(String(200), nullable=True)
    open_today_bal = Column(String(200), nullable=True)
    open_month_bal = Column(String(200), nullable=True)
    open_fiscal_year_bal = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)
    table_id = Column(Integer, ForeignKey("tabledef.id"))
    tabledef = relationship("TableDef", foreign_keys=[table_id])


class OpCashDpstWdrl(Base):
    __tablename__ = "opcashdpstwdrl"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    account_type = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    transaction_catg = Column(String(200), nullable=True)
    transaction_catg_desc = Column(String(200), nullable=True)
    transaction_today_amt = Column(String(200), nullable=True)
    transaction_mtd_amt = Column(String(200), nullable=True)
    transaction_fytd_amt = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)
    table_id = Column(Integer, ForeignKey("tabledef.id"))
    tabledef = relationship("TableDef", foreign_keys=[table_id])


class PubDebtTrans(Base):
    __tablename__ = "pubdebttrans"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    security_market = Column(String(200), nullable=True)
    security_type = Column(String(200), nullable=True)
    security_type_desc = Column(String(200), nullable=True)
    transaction_today_amt = Column(String(200), nullable=True)
    transaction_mtd_amt = Column(String(200), nullable=True)
    transaction_fytd_amt = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)
    table_id = Column(Integer, ForeignKey("tabledef.id"))
    tabledef = relationship("TableDef", foreign_keys=[table_id])


class PubDebtCashAdj(Base):
    __tablename__ = "pubdebtcashadj"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    adj_type = Column(String(200), nullable=True)
    adj_type_desc = Column(String(200), nullable=True)
    adj_today_amt = Column(String(200), nullable=True)
    adj_mtd_amt = Column(String(200), nullable=True)
    adj_fytd_amt = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)
    table_id = Column(Integer, ForeignKey("tabledef.id"))
    tabledef = relationship("TableDef", foreign_keys=[table_id])


class DebtSubjLim(Base):
    __tablename__ = "debtsubjlim"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    debt_catg = Column(String(200), nullable=True)
    debt_catg_desc = Column(String(200), nullable=True)
    close_today_bal = Column(String(200), nullable=True)
    open_today_bal = Column(String(200), nullable=True)
    open_month_bal = Column(String(200), nullable=True)
    open_fiscal_year_bal = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)
    table_id = Column(Integer, ForeignKey("tabledef.id"))
    tabledef = relationship("TableDef", foreign_keys=[table_id])


class FedTaxDpst(Base):
    __tablename__ = "fedtaxdpst"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    tax_deposit_type = Column(String(200), nullable=True)
    tax_deposit_type_desc = Column(String(200), nullable=True)
    tax_deposit_today_amt = Column(String(200), nullable=True)
    tax_deposit_mtd_amt = Column(String(200), nullable=True)
    tax_deposit_fytd_amt = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)
    table_id = Column(Integer, ForeignKey("tabledef.id"))
    tabledef = relationship("TableDef", foreign_keys=[table_id])


class TaxLoanNtBDepCat(Base):
    __tablename__ = "taxLoanntbdepcat"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    transaction_type_desc = Column(String(200), nullable=True)
    depositary_type_a_amt = Column(String(200), nullable=True)
    depositary_type_b_amt = Column(String(200), nullable=True)
    depositary_type_c_amt = Column(String(200), nullable=True)
    total_amt = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)
    table_id = Column(Integer, ForeignKey("tabledef.id"))
    tabledef = relationship("TableDef", foreign_keys=[table_id])


class StCashInvest(Base):
    __tablename__ = "stcashinvest"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    transaction_type = Column(String(200), nullable=True)
    transaction_type_desc = Column(String(200), nullable=True)
    depositary_type_a_amt = Column(String(200), nullable=True)
    depositary_type_b_amt = Column(String(200), nullable=True)
    depositary_type_c_amt = Column(String(200), nullable=True)
    total_amt = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)
    table_id = Column(Integer, ForeignKey("tabledef.id"))
    tabledef = relationship("TableDef", foreign_keys=[table_id])


class IncmTaxRfnd(Base):
    __tablename__ = "incmtaxrfnd"

    id = Column(Integer, primary_key=True)
    record_date = Column(String(200), nullable=True)
    tax_refund_type = Column(String(200), nullable=True)
    tax_refund_type_desc = Column(String(200), nullable=True)
    tax_refund_today_amt = Column(String(200), nullable=True)
    tax_refund_mtd_amt = Column(String(200), nullable=True)
    tax_refund_fytd_amt = Column(String(200), nullable=True)
    sub_table_name = Column(String(200), nullable=True)
    src_line_nbr = Column(String(200), nullable=True)
    record_fiscal_year = Column(String(200), nullable=True)
    record_fiscal_quarter = Column(String(200), nullable=True)
    record_calendar_year = Column(String(200), nullable=True)
    record_calendar_quarter = Column(String(200), nullable=True)
    record_calendar_month = Column(String(200), nullable=True)
    record_calendar_day = Column(String(200), nullable=True)
    table_id = Column(Integer, ForeignKey("tabledef.id"))
    tabledef = relationship("TableDef", foreign_keys=[table_id])


def insert(objects):
    try:
        with Session(engine) as session:
            session.bulk_save_objects(objects)
            session.commit()
    except IntegrityError as err:
        pass

def select(object):
    result_set = None
    with Session(engine) as session:
        result_set = session.query(object)

    return result_set

for opcashbal in select(OpCashBal):
    print(opcashbal.tabledef.table_name)


Base.metadata.create_all(engine, checkfirst=True)
objects = [
    TableDef(id=1, table_name="Operating Cash Balance", table_nbr="I"),
    TableDef(
        id=2, table_name="Deposits and Withdrawals of Operating Cash", table_nbr="II"
    ),
    TableDef(id=3, table_name="Public Debt Transactions", table_nbr="III-A"),
    TableDef(
        id=4,
        table_name="Adjustment of Public Debt Transactions to Cash Basis",
        table_nbr="III-B",
    ),
    TableDef(id=5, table_name="Debt Subject to Limit", table_nbr="III-C"),
    TableDef(id=6, table_name="Federal Tax Deposits", table_nbr="IV"),
    TableDef(
        id=7,
        table_name="Tax and Loan Note Accounts by Depositary Category",
        table_nbr="V",
    ),
    TableDef(id=8, table_name="Short Term Cash Investments", table_nbr="V"),
    TableDef(id=9, table_name="Income Tax Refunds Issued", table_nbr="VI"),
]
insert(objects)
