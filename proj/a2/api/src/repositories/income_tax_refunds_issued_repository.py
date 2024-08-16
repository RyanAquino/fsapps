from api.src.models.dts_table_models import Income_Tax_Refunds_Issued
from api.src.repositories.dts_tables_repository import DTSTablesBaseRepository


class IncomeTaxRefundsIssuedRepository(DTSTablesBaseRepository):
    name = "income_tax_refunds_issued"

    def get_all(self):
        with self.session_factory() as session:
            return session.query(Income_Tax_Refunds_Issued).all()

    def generate_filter(self):
        pass
