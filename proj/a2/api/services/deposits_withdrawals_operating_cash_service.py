from api.repositories.dts_tables_repository import DTSTablesBaseRepository
from api.schemas.schemas import DepositsWithdrawalsOperatingCashDBSchema
from api.services.dts_table_base_service import DTSBaseService


class DepositsWithdrawalsOperatingCashBalanceService(DTSBaseService):
    def __init__(self, dts_table_repository: DTSTablesBaseRepository, service):
        super().__init__(dts_table_repository, service)

    def get_data(self, filters):
        data = self._repository.get_all()
        serialized_items = [
            DepositsWithdrawalsOperatingCashDBSchema.model_validate(item)
            for item in data
        ]
        json_data = [item.model_dump() for item in serialized_items]
        return json_data
