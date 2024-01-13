from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from api import config

engine = create_engine(config.settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
