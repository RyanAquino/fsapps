from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from api.src.models.spy_finance_models import SPYFinance


class SPYFinanceRepository:

    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def get_all(self):
        with self.session_factory() as session:
            q = session.query(SPYFinance).order_by(SPYFinance.record_date.asc())
            return q.all()
