import pandas as pd

from api.repositories.dts_tables_repository import DTSTablesBaseRepository
from api.schemas.schemas import OperatingCashBalanceDBSchema
from api.services.dts_table_base_service import DTSBaseService


class OperatingCashBalanceService(DTSBaseService):
    def __init__(self, dts_table_repository: DTSTablesBaseRepository, service):
        super().__init__(dts_table_repository, service)

    def get_data(self, filters):
        data = self._repository.get_all()
        serialized_items = [
            OperatingCashBalanceDBSchema.model_validate(item) for item in data
        ]
        json_data = [item.model_dump() for item in serialized_items]
        df = pd.DataFrame(json_data)

        net_change_df = self.calculate_day_net_change(df)
        df = df.merge(
            net_change_df[["net_change", "record_date"]], how="inner", on="record_date"
        )

        json_data = df.to_dict(orient="records")
        return json_data

    @staticmethod
    def calculate_day_net_change(df: pd.DataFrame) -> pd.DataFrame:
        opening_balance = df.loc[
            df["account_type"] == "Treasury General Account (TGA) Opening Balance"
        ]
        closing_balance = df.loc[
            df["account_type"] == "Treasury General Account (TGA) Closing Balance"
        ]
        balance = opening_balance.merge(
            closing_balance,
            left_on="record_date",
            right_on="record_date",
            suffixes=("_opening", "_closing"),
        )
        open_close_bal = balance[
            ["record_date", "open_today_bal_opening", "open_today_bal_closing"]
        ]
        open_close_bal["net_change"] = open_close_bal.apply(
            lambda row: row.open_today_bal_opening - row.open_today_bal_closing, axis=1
        )

        return open_close_bal
