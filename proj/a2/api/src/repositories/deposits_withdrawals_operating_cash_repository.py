from api.src.models.dts_table_models import Deposits_Withdrawals_Operating_Cash
from api.src.repositories.dts_tables_repository import DTSTablesBaseRepository


class DepositsWithdrawalsOperatingCashBalanceRepository(DTSTablesBaseRepository):
    name = "deposits_withdrawals_operating_cash_balance"

    def get_all(self):
        _, fields = self.generate_filter()
        with self.session_factory() as session:
            columns = [
                getattr(Deposits_Withdrawals_Operating_Cash, field) for field in fields
            ]
            q = session.query(*columns).order_by(Deposits_Withdrawals_Operating_Cash.record_date.desc())
            return q.all()

    def generate_filter(self):
        query_filter = {}

        return query_filter, (
            "id",
            "transaction_type",
            "transaction_catg",
            "account_type",
            "record_date",
            "transaction_today_amt",
        )
