from abc import ABC

from api.src.repositories.dts_tables_repository import DTSTablesBaseRepository


class DTSBaseService(ABC):
    def __init__(self, dts_table_repository: DTSTablesBaseRepository, service):
        self._repository = dts_table_repository
        self._service = service

    def get_data(self, filters):
        pass
