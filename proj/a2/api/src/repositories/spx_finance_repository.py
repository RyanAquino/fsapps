from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from api.src.models.spx_finance_models import SPXFinanceOptions


class SPXFinanceRepository:

    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def get_options(self):
        _, fields = self.generate_filter()
        with self.session_factory() as session:
            columns = [getattr(SPXFinanceOptions, field) for field in fields]
            q = session.query(*columns)
            return q.all()

    @staticmethod
    def generate_filter():
        query_filter = {}

        return query_filter, (
            "id",
            "last_price",
            "bid",
            "ask",
            "volume",
            "open_interest",
            "strike",
            "last_trade_date",
        )
