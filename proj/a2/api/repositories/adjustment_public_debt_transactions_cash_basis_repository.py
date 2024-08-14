from api.models.dts_table_models import Adjustment_Public_Debt_Transactions_Cash_Basis
from api.repositories.dts_tables_repository import DTSTablesBaseRepository


class AdjustmentPublicDebtTransactionsCashBasisRepository(DTSTablesBaseRepository):
    name = "adjustment_public_debt_transactions_cash_basis"

    def get_data(self):
        with self.session_factory() as session:
            return session.query(Adjustment_Public_Debt_Transactions_Cash_Basis).all()

    def generate_filter(self):
        pass
