from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

engine = create_engine("mysql+pymysql://root:@localhost/dts_tables",echo = False)


class Base(DeclarativeBase):
    pass

class OpCashBal(Base):
    __tablename__ = "opcashbal"
    tabledesc = "Operating Cash Balance"

    id = Column(Integer, primary_key = True)
    record_date = Column(String(200))
    account_type = Column(String(200))
    close_today_bal = Column(String(200))
    open_today_bal = Column(String(200))
    open_month_bal = Column(String(200))
    open_fiscal_year_bal = Column(String(200))
    table_nbr = Column(String(200))
    table_name = Column(String(200))
    sub_table_name = Column(String(200))
    src_line_nbr = Column(String(200))
    record_fiscal_year = Column(String(200))
    record_fiscal_quarter = Column(String(200))
    record_calendar_year = Column(String(200))
    record_calendar_quarter = Column(String(200))
    record_calendar_month = Column(String(200))
    record_calendar_day = Column(String(200))

class OpCashDpstWdrl(Base):
    __tablename__ = "opcashdpstwdrl"
    tabledesc = "Deposits and Withdrawals of Operating Cash"

    id = Column(Integer, primary_key = True)
    record_date = Column(String(200))
    account_type = Column(String(200))
    transaction_type = Column(String(200))
    transaction_catg = Column(String(200))
    transaction_catg_desc = Column(String(200))
    transaction_today_amt = Column(String(200))
    transaction_mtd_amt = Column(String(200))
    transaction_fytd_amt = Column(String(200))
    table_nbr = Column(String(200))
    table_name = Column(String(200))
    src_line_nbr = Column(String(200))
    record_fiscal_year = Column(String(200))
    record_fiscal_quarter = Column(String(200))
    record_calendar_year = Column(String(200))
    record_calendar_quarter = Column(String(200))
    record_calendar_month = Column(String(200))
    record_calendar_day = Column(String(200))

class PubDebtTrans(Base):
    __tablename__ = "pubdebttrans"
    tabledesc = "Public Debt Transactions"  

    id = Column(Integer, primary_key = True)
    record_date = Column(String(200))
    transaction_type = Column(String(200))
    security_market = Column(String(200))
    security_type = Column(String(200))
    security_type_desc = Column(String(200))
    transaction_today_amt = Column(String(200))
    transaction_mtd_amt = Column(String(200))
    transaction_fytd_amt = Column(String(200))
    table_nbr = Column(String(200))
    table_name = Column(String(200))
    src_line_nbr = Column(String(200))
    record_fiscal_year = Column(String(200))
    record_fiscal_quarter = Column(String(200))
    record_calendar_year = Column(String(200))
    record_calendar_quarter = Column(String(200))
    record_calendar_month = Column(String(200))
    record_calendar_day = Column(String(200))
    
class PubDebtCashAdj(Base):
    __tablename__ = "pubdebtcashadj"
    tabledesc = "Adjustment of Public Debt Transactions to Cash Basis"

    id = Column(Integer, primary_key = True)
    record_date = Column(String(200))
    transaction_type = Column(String(200))
    adj_type = Column(String(200))
    adj_type_desc = Column(String(200))
    adj_today_amt = Column(String(200))
    adj_mtd_amt = Column(String(200))
    adj_fytd_amt = Column(String(200))
    table_nbr = Column(String(200))
    table_name = Column(String(200))
    sub_table_name = Column(String(200))
    src_line_nbr = Column(String(200))
    record_fiscal_year = Column(String(200))
    record_fiscal_quarter = Column(String(200))
    record_calendar_year = Column(String(200))
    record_calendar_quarter = Column(String(200))
    record_calendar_month = Column(String(200))
    record_calendar_day = Column(String(200))

class DebtSubjLim(Base):
    __tablename__ = "debtsubjlim"
    tabledesc = "Debt Subject to Limit"

    id = Column(Integer, primary_key = True)
    record_date = Column(String(200))
    debt_catg = Column(String(200))
    debt_catg_desc = Column(String(200))
    close_today_bal = Column(String(200))
    open_today_bal = Column(String(200))
    open_month_bal = Column(String(200))
    open_fiscal_year_bal = Column(String(200))
    table_nbr = Column(String(200))
    table_name = Column(String(200))
    sub_table_name = Column(String(200))
    src_line_nbr = Column(String(200))
    record_fiscal_year = Column(String(200))
    record_fiscal_quarter = Column(String(200))
    record_calendar_year = Column(String(200))
    record_calendar_quarter = Column(String(200))
    record_calendar_month = Column(String(200))
    record_calendar_day = Column(String(200))

class FedTaxDpst(Base):
    __tablename__ = "fedtaxdpst"
    tabledesc = "Federal Tax Deposits"

    id = Column(Integer, primary_key = True)
    record_date = Column(String(200))
    tax_deposit_type = Column(String(200))
    tax_deposit_type_desc = Column(String(200))
    tax_deposit_today_amt = Column(String(200))
    tax_deposit_mtd_amt = Column(String(200))
    tax_deposit_fytd_amt = Column(String(200))
    table_nbr = Column(String(200))
    table_name = Column(String(200))
    sub_table_name = Column(String(200))
    src_line_nbr = Column(String(200))
    record_fiscal_year = Column(String(200))
    record_fiscal_quarter = Column(String(200))
    record_calendar_year = Column(String(200))
    record_calendar_quarter = Column(String(200))
    record_calendar_month = Column(String(200))
    record_calendar_day = Column(String(200))

class TaxLoanNtBDepCat(Base):
    __tablename__ = "taxLoanntbdepcat"
    tabledesc = "Tax and Loan Note Accounts by Depositary Category"

    id = Column(Integer, primary_key = True)
    record_date = Column(String(200))
    transaction_type = Column(String(200)) 
    transaction_type_desc = Column(String(200)) 
    depositary_type_a_amt = Column(String(200)) 
    depositary_type_b_amt = Column(String(200)) 
    depositary_type_c_amt = Column(String(200)) 
    total_amt = Column(String(200)) 
    table_nbr = Column(String(200)) 
    table_name = Column(String(200)) 
    sub_table_name = Column(String(200)) 
    src_line_nbr = Column(String(200)) 
    record_fiscal_year = Column(String(200)) 
    record_fiscal_quarter = Column(String(200)) 
    record_calendar_year = Column(String(200)) 
    record_calendar_quarter = Column(String(200)) 
    record_calendar_month = Column(String(200)) 
    record_calendar_day = Column(String(200)) 

class StCashInvest(Base):
    __tablename__ = "stcashinvest"
    tabledesc = "Short Term Cash Investments"

    id = Column(Integer, primary_key = True)
    record_date = Column(String(200))
    transaction_type = Column(String(200))
    transaction_type_desc = Column(String(200))
    depositary_type_a_amt = Column(String(200))
    depositary_type_b_amt = Column(String(200))
    depositary_type_c_amt = Column(String(200))
    total_amt = Column(String(200))
    table_nbr = Column(String(200))
    table_name = Column(String(200))
    sub_table_name = Column(String(200))
    src_line_nbr = Column(String(200))
    record_fiscal_year = Column(String(200))
    record_fiscal_quarter = Column(String(200))
    record_calendar_year = Column(String(200))
    record_calendar_quarter = Column(String(200))
    record_calendar_month = Column(String(200))
    record_calendar_day = Column(String(200))

class IncmTaxRfnd(Base):
    __tablename__ = "incmtaxrfnd"
    tabledesc = "Income Tax Refunds Issued"

    id = Column(Integer, primary_key = True)
    record_date = Column(String(200))
    tax_refund_type = Column(String(200))
    tax_refund_type_desc = Column(String(200))
    tax_refund_today_amt = Column(String(200))
    tax_refund_mtd_amt = Column(String(200))
    tax_refund_fytd_amt = Column(String(200))
    table_nbr = Column(String(200))
    table_name = Column(String(200))
    sub_table_name = Column(String(200))
    src_line_nbr = Column(String(200))
    record_fiscal_year = Column(String(200))
    record_fiscal_quarter = Column(String(200))
    record_calendar_year = Column(String(200))
    record_calendar_quarter = Column(String(200))
    record_calendar_month = Column(String(200))
    record_calendar_day = Column(String(200))

def insert(objects):
    with Session(engine) as session:
        session.bulk_save_objects(objects)
        session.commit()
    

Base.metadata.create_all(engine, checkfirst=True)