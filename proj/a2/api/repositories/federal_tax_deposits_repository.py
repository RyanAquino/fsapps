from api.models.dts_table_models import Federal_Tax_Deposits
from api.repositories.dts_tables_repository import DTSTablesBaseRepository


class FederalTaxDepositsRepository(DTSTablesBaseRepository):
    name = "federal_tax_deposits"

    def get_all(self):
        with self.session_factory() as session:
            return session.query(Federal_Tax_Deposits).all()

    def generate_filter(self):
        pass
