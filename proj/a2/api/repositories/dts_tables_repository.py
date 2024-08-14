from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod


class DTSTablesBaseRepository(ABC):
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def generate_filter(self):
        pass
