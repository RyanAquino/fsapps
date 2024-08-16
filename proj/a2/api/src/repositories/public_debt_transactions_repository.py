from api.src.models.dts_table_models import Public_Debt_Transactions
from api.src.repositories.dts_tables_repository import DTSTablesBaseRepository


class PublicDebtTransactionsRepository(DTSTablesBaseRepository):
    name = "public_debt_transactions"

    def get_all(self):
        with self.session_factory() as session:
            return session.query(Public_Debt_Transactions).all()

    def generate_filter(self):
        pass
