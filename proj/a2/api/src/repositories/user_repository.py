from contextlib import AbstractContextManager
from typing import Callable, Type

from sqlalchemy.orm import Session

from api.src.models.models import User


class UserRepository:

    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def get_all(self) -> list[Type[User]]:
        with self.session_factory() as session:
            return session.query(User).all()

    def get_by_id(self, user_id: int) -> User:
        with self.session_factory() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                raise UserNotFoundError(user_id)
            return user

    def get_by_username(self, username: str) -> User:
        with self.session_factory() as session:
            user = session.query(User).filter(User.username == username).first()
            if not user:
                raise UserNotFoundError(username)
            return user

    def add(self, username: str, password: str, is_active: bool = True) -> User:
        with self.session_factory() as session:
            user = User(
                username=username, hashed_password=password, is_active=is_active
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_by_id(self, user_id: int) -> None:
        with self.session_factory() as session:
            entity: User = session.query(User).filter(User.id == user_id).first()
            if not entity:
                raise UserNotFoundError(user_id)
            session.delete(entity)
            session.commit()


class NotFoundError(Exception):

    def __init__(self, entity_name: str):
        super().__init__(f"{entity_name} not found")


class UserNotFoundError(NotFoundError):
    """
    User not found
    """
