from sqlalchemy import Boolean, Column, Integer, String

from api.database import Base


class User(Base):
    """Column model for registered_users"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
