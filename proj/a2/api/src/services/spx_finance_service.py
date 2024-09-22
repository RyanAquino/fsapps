from api.src.repositories.spx_finance_repository import SPXFinanceRepository
from api.src.schemas.schemas import SPXFinanceOptionsDBSchema


class SPXFinanceService:

    def __init__(self, spx_finance_repository: SPXFinanceRepository):
        self._repository = spx_finance_repository

    def get_options_data(self):
        data = self._repository.get_options()
        serialized_items = [
            SPXFinanceOptionsDBSchema.model_validate(item) for item in data
        ]
        json_data = [item.model_dump(exclude_none=True) for item in serialized_items]
        return json_data
