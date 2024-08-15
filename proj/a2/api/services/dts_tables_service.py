from typing import Callable, Optional

from api.repositories.dts_tables_repository import DTSTablesBaseRepository
from api.services.adjustment_public_debt_transactions_cash_basis_service import (
    AdjustmentPublicDebtTransactionsCashBasisService,
)
from api.services.operating_cash_balance_service import OperatingCashBalanceService


class DTSTablesService:
    def __init__(self, dts_tables_repository: dict[str, DTSTablesBaseRepository]):
        self._repository = dts_tables_repository

    def get_repository(self, table_name: str) -> DTSTablesBaseRepository:
        repository: Optional[Callable] = self._repository.get(table_name)

        if not repository:
            raise InvalidTable

        return repository()

    def get_service(self, table_name: str):
        repository = self.get_repository(table_name)
        table_service_mappings = {
            "operating_cash_balance": OperatingCashBalanceService,
            "adjustment_public_debt_transactions_cash_basis": AdjustmentPublicDebtTransactionsCashBasisService,
        }
        service = table_service_mappings.get(table_name)

        return service(repository, service)

    def get_data(self, table_name, filters=None):
        service = self.get_service(table_name)
        data = service.get_data(filters)
        return data


class InvalidTable(Exception):
    def __init__(self, table_name):
        super().__init__(f"Invalid table name: {table_name}")
