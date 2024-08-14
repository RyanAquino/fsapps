from typing import Callable, Optional
from api.repositories.dts_tables_repository import DTSTablesBaseRepository


class DTSTablesService:
    def __init__(self, dts_tables_repository: dict[str, DTSTablesBaseRepository]):
        self._repository = dts_tables_repository

    def get_repository(self, table_name: str) -> DTSTablesBaseRepository:
        repository: Optional[Callable] = self._repository.get(table_name)

        if not repository:
            raise InvalidTable

        return repository()

    def get_data(self, table_name, filters=None):
        repository = self.get_repository(table_name)
        data = repository.get_data()
        return data


class InvalidTable(Exception):
    def __init__(self, table_name):
        super().__init__(f"Invalid table name: {table_name}")
