from sqlalchemy.sql import text
from api.database import SessionLocal
from api.models.dts_table_models import (
    Operating_Cash_Balance,
    Deposits_Withdrawals_Operating_Cash,
    Public_Debt_Transactions,
    Adjustment_Public_Debt_Transactions_Cash_Basis,
    Debt_Subject_To_Limit,
    Inter_Agency_Tax_Transfers,
    Income_Tax_Refunds_Issued,
    Federal_Tax_Deposits,
    Short_Term_Cash_Investments,
)


class DTSTableOperations:
    def __init__(self, db: SessionLocal):
        self.dts_tables = {
            "Operating Cash Balance": Operating_Cash_Balance,
            "Deposits and Withdrawals of Operating Cash": Deposits_Withdrawals_Operating_Cash,
            "Public Debt Transactions": Public_Debt_Transactions,
            "Adjustment of Public Debt Transactions to Cash Basis": Adjustment_Public_Debt_Transactions_Cash_Basis,
            "Debt Subject to Limit": Debt_Subject_To_Limit,
            "Inter-agency Tax Transfers": Inter_Agency_Tax_Transfers,
            "Income Tax Refunds Issued": Income_Tax_Refunds_Issued,
            "Federal Tax Deposits": Federal_Tax_Deposits,
            "Short-Term Cash Investments": Short_Term_Cash_Investments,
        }
        self.db = db

    def get_filtered_data(self, table_name: str, **filters):
        table = None
        """Return filtered data from dts tables"""
        for table_obj in self.dts_tables.values():
            if table_obj.__name__.lower() == table_name.lower():
                table = table_obj
                break

        statement = self.db.query(table)
        for key, value in filters.items():
            if value is not None:
                filt = key + "=" + value
                statement = statement.filter(text(filt))
        return statement.all()
