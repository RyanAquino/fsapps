from sqlalchemy import Column, DateTime, Float, Integer

from api.src.database import Base


class SPYFinance(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """SPY Finance."""
    __tablename__ = "spy_finance"

    id = Column(Integer, primary_key=True)
    record_date = Column(DateTime(), nullable=True)
    open = Column(Float(), nullable=True)
    high = Column(Float(), nullable=True)
    low = Column(Float(), nullable=True)
    close = Column(Float(), nullable=True)
    adj_close = Column(Float(), nullable=True)
    volume = Column(Integer(), nullable=True)
