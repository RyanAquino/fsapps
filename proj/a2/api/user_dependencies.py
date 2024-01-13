from api.database import SessionLocal


# Dependency
def init_db():
    """Initialize the db generator"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
