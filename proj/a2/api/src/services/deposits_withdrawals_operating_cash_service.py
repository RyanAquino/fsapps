import pandas as pd

from api.src.repositories.dts_tables_repository import DTSTablesBaseRepository
from api.src.schemas.schemas import DepositsWithdrawalsOperatingCashDBSchema
from api.src.services.dts_table_base_service import DTSBaseService


class DepositsWithdrawalsOperatingCashBalanceService(DTSBaseService):
    def __init__(self, dts_table_repository: DTSTablesBaseRepository, service):
        super().__init__(dts_table_repository, service)

    def get_data(self, filters):
        data = self._repository.get_all()

        if not data:
            return []

        serialized_items = [
            DepositsWithdrawalsOperatingCashDBSchema.model_validate(item)
            for item in data
        ]
        json_data = [item.model_dump(exclude_none=True) for item in serialized_items]

        df = pd.DataFrame(json_data)
        daily_deposit_withdrawal_totals = (
            self.calculate_daily_deposits_withdrawals_total(df)
        )
        df = df.merge(daily_deposit_withdrawal_totals, how="inner", on="record_date")

        json_data = df.to_dict(orient="records")

        return json_data

    @staticmethod
    def calculate_daily_deposits_withdrawals_total(df: pd.DataFrame):
        deposits_filter = (
            (df["transaction_type"] == "Deposits")
            & (df["transaction_catg"] != "Public Debt Cash Issues (Table IIIB)")
            & (df["account_type"] != "Treasury General Account Total Deposits")
        )

        deposits = df[deposits_filter][["record_date", "transaction_today_amt"]]
        deposits = deposits.astype({"transaction_today_amt": float})
        deposits = deposits.groupby("record_date")["transaction_today_amt"].sum()

        withdrawals_filter = (
            (df["transaction_type"] == "Withdrawals")
            & (df["transaction_catg"] != "Public Debt Cash Redemp. (Table IIIB)")
            & (df["account_type"] != "Treasury General Account Total Withdrawals")
        )

        withdrawals = df[withdrawals_filter][["record_date", "transaction_today_amt"]]
        withdrawals = withdrawals.astype({"transaction_today_amt": float})
        withdrawals = withdrawals.groupby("record_date")["transaction_today_amt"].sum()

        deposit_withdrawals = deposits.to_frame().merge(
            withdrawals,
            how="inner",
            on="record_date",
            suffixes=("_deposits", "_withdrawals"),
        )
        deposit_withdrawals["total_transaction_today"] = deposit_withdrawals.apply(
            lambda row: row["transaction_today_amt_deposits"]
            - row["transaction_today_amt_withdrawals"],
            axis=1,
        )

        return deposit_withdrawals
