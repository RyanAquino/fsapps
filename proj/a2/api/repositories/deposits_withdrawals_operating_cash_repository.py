from api.models.dts_table_models import Deposits_Withdrawals_Operating_Cash
from api.repositories.dts_tables_repository import DTSTablesBaseRepository


class DepositsWithdrawalsOperatingCashBalanceRepository(DTSTablesBaseRepository):
    name = "deposits_withdrawals_operating_cash_balance"

    def get_data(self):
        with self.session_factory() as session:
            return session.query(Deposits_Withdrawals_Operating_Cash).all()

    def generate_filter(self):
        pass
