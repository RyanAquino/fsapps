from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String

from api.src.database import Base


class SPXFinanceOptions(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """SPY Finance options."""
    __tablename__ = "spy_finance_opts"

    id = Column(Integer, primary_key=True)
    contract_name = Column(String(length=200), nullable=True)
    last_trade_date = Column(DateTime(), nullable=True)
    strike = Column(Integer(), nullable=True)
    last_price = Column(Float(), nullable=True)
    bid = Column(Float(), nullable=True)
    ask = Column(Float(), nullable=True)
    change = Column(Float(), nullable=True)
    change_percent = Column(Float(), nullable=True)
    volume = Column(Integer(), nullable=True)
    open_interest = Column(Integer(), nullable=True)
    implied_volatility = Column(Float(), nullable=True)
    calls = Column(Boolean(), default=False)
    in_the_money = Column(Boolean(), default=False)
