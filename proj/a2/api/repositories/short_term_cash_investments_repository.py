from api.models.dts_table_models import Short_Term_Cash_Investments
from api.repositories.dts_tables_repository import DTSTablesBaseRepository


class ShortTermCashInvestmentsRepository(DTSTablesBaseRepository):
    name = "short_term_cash_investments"

    def get_all(self):
        with self.session_factory() as session:
            return session.query(Short_Term_Cash_Investments).all()

    def generate_filter(self):
        pass
