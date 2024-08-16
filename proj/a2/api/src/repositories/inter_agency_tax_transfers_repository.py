from api.src.models.dts_table_models import Inter_Agency_Tax_Transfers
from api.src.repositories.dts_tables_repository import DTSTablesBaseRepository


class InterAgencyTaxTransfersRepository(DTSTablesBaseRepository):
    name = "inter_agency_tax_transfers"

    def get_all(self):
        with self.session_factory() as session:
            return session.query(Inter_Agency_Tax_Transfers).all()

    def generate_filter(self):
        pass
