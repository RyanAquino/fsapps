from api.src.repositories.dts_tables_repository import DTSTablesBaseRepository
from api.src.schemas.schemas import IncomeTaxRefundsIssuedDBSchema
from api.src.services.dts_table_base_service import DTSBaseService


class IncomeTaxRefundsIssuedService(DTSBaseService):
    def __init__(self, dts_table_repository: DTSTablesBaseRepository, service):
        super().__init__(dts_table_repository, service)

    def get_data(self, filters):
        data = self._repository.get_all()
        serialized_items = [
            IncomeTaxRefundsIssuedDBSchema.model_validate(item) for item in data
        ]
        json_data = [item.model_dump() for item in serialized_items]
        return json_data
