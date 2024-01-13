from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from api.config import settings
from api.database import SessionLocal
from api.models import models
from api.models.models import User
from api.schemas import schemas


class AccessUser:
    @staticmethod
    def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
        """Create user in the database"""
        db_user = models.User(
            email=user.email, hashed_password=hashed_password, is_enabled=True
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


class UserOperations:
    def __init__(self, db: SessionLocal):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/auth/login")
        self.db = db

    def get_request_user(self, username: str) -> Optional[User]:
        """Get the user information from the database using username"""
        user = self.db.query(User).where(User.username == username).first()
        if not user:
            return None
        return user

    def get_current_user(self):
        """Get the current logged-in user and check if it is authenticated"""
        token: str = Depends(self.oauth2_scheme)
        credential_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
            username: str = payload.get("username")
            if username is None:
                raise credential_exception

            token_data = schemas.TokenData(username=username)
        except JWTError:
            raise credential_exception

        user = self.get_request_user(username=token_data.username)
        if user is None:
            raise credential_exception

        return user

    def get_current_active_user(self):
        """Check if the token of the logged-in user is still active"""
        current_user: schemas.User = self.get_current_user()
        if not current_user.enabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return
