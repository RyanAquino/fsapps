from api.repositories.dts_tables_repository import DTSTablesBaseRepository
from api.schemas.schemas import OperatingCashBalanceDBSchema
from api.services.dts_table_base_service import DTSBaseService


class OperatingCashBalanceService(DTSBaseService):
    def __init__(self, dts_table_repository: DTSTablesBaseRepository, service):
        super().__init__(dts_table_repository, service)

    def get_data(self, filters):
        data = self._repository.get_all()
        serialized_items = [
            OperatingCashBalanceDBSchema.model_validate(item) for item in data if item.close_today_bal != "null"
        ]
        json_data = []

        for item in serialized_items:
            item_data = item.model_dump()
            item_data["net_change"] = int(item.open_today_bal) - int(item.close_today_bal)
            json_data.append(item_data)

        return json_data
