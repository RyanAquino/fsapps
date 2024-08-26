from api.src.repositories.aaii_sentiment_repository import AAIISentimentRepository
from api.src.schemas.schemas import AAIISentimentDBSchema


class AAIISentimentService:

    def __init__(self, aaii_sentiment_repository: AAIISentimentRepository):
        self._repository = aaii_sentiment_repository

    def get_data(self):
        data = self._repository.get_all()
        serialized_items = [AAIISentimentDBSchema.model_validate(item) for item in data]
        json_data = [item.model_dump(exclude_none=True) for item in serialized_items]
        return json_data
