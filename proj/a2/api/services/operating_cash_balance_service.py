from api.repositories.dts_tables_repository import DTSTablesBaseRepository
from api.services.dts_table_base_service import DTSBaseService


class OperatingCashBalanceService(DTSBaseService):
    def __init__(self, dts_table_repository: DTSTablesBaseRepository, service):
        super().__init__(dts_table_repository, service)

    def get_data(self, filters):
        # Business logic here
        return self._repository.get_all()
