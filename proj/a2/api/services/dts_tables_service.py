from typing import Callable, Optional

from sqlalchemy.sql import text
from api.models.dts_table_models import (
    Operating_Cash_Balance,
    Deposits_Withdrawals_Operating_Cash,
    Public_Debt_Transactions,
    Adjustment_Public_Debt_Transactions_Cash_Basis,
    Debt_Subject_To_Limit,
    Inter_Agency_Tax_Transfers,
    Income_Tax_Refunds_Issued,
    Federal_Tax_Deposits,
    Short_Term_Cash_Investments,
)
from api.repositories.dts_tables_repository import DTSTablesBaseRepository


class DTSTablesService:
    def __init__(self, dts_tables_repository: dict[str, DTSTablesBaseRepository]):
        self._repository = dts_tables_repository

    def get_repository(self, table_name: str) -> Callable:
        repository: Optional[Callable] = self._repository.get(table_name)

        if not repository:
            raise InvalidTable

        return repository

    def get_data(self, table_name, filters=None):
        repository = self.get_repository(table_name)()
        data = repository.get_data()
        return data


class InvalidTable(Exception):
    def __init__(self, table_name):
        super().__init__(f"Invalid table name: {table_name}")
