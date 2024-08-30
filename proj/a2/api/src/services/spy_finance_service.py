from api.src.repositories.spy_finance_repository import SPYFinanceRepository
from api.src.schemas.schemas import SPYFinanceDBSchema


class SPYFinanceService:

    def __init__(self, spy_finance_repository: SPYFinanceRepository):
        self._repository = spy_finance_repository

    def get_data(self):
        data = self._repository.get_all()
        serialized_items = [SPYFinanceDBSchema.model_validate(item) for item in data]
        json_data = [item.model_dump(exclude_none=True) for item in serialized_items]
        return json_data
