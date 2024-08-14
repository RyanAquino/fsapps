from api.models.dts_table_models import Operating_Cash_Balance
from api.repositories.dts_tables_repository import DTSTablesBaseRepository


class OperatingCashBalanceRepository(DTSTablesBaseRepository):
    name = "operating_cash_balance"

    def get_all(self):
        with self.session_factory() as session:
            return session.query(Operating_Cash_Balance).all()

    def generate_filter(self):
        pass
