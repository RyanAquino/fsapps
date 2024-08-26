from sqlalchemy import Column, Float, Integer, String

from api.src.database import Base


class AAIISentiment(Base):
    # pylint:disable=too-few-public-methods,invalid-name
    """DTS Table 1."""
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
