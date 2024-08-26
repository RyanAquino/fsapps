import datetime
from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session

from api.src.models.aaii_sentiment_models import AAIISentiment


class AAIISentimentRepository:

    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    def get_all(self):
        _, fields = self.generate_filter()
        last_years = datetime.datetime.now() - datetime.timedelta(days=1095)
        with self.session_factory() as session:
            columns = [getattr(AAIISentiment, field) for field in fields]
            q = session.query(*columns).filter(AAIISentiment.record_date >= last_years)
            return q.all()

    @staticmethod
    def generate_filter():
        query_filter = {}

        return query_filter, (
            "id",
            "record_date",
            "bearish",
            "neutral",
            "bullish",
        )
