from api.src.models.dts_table_models import Deposits_Withdrawals_Operating_Cash
from api.src.repositories.dts_tables_repository import DTSTablesBaseRepository


class DepositsWithdrawalsOperatingCashBalanceRepository(DTSTablesBaseRepository):
    name = "deposits_withdrawals_operating_cash_balance"

    def get_all(self):
        with self.session_factory() as session:
            return session.query(Deposits_Withdrawals_Operating_Cash).all()

    def generate_filter(self):
        pass
