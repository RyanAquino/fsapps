from contextlib import AbstractContextManager
from typing import Callable, Type
from sqlalchemy.orm import Session
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
from abc import ABC, abstractmethod


class DTSTablesBaseRepository(ABC):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def generate_filter(self):
        pass


class OperatingCashBalanceRepository(DTSTablesBaseRepository):
    name = "operating_cash_balance"

    def get_data(self):
        with self.session_factory() as session:
            return session.query(Operating_Cash_Balance).all()

    def generate_filter(self):
        pass

    # def get_deposits_withdrawals_operating_cash(self):
    #     with self.session_factory() as session:
    #         return session.query(Deposits_Withdrawals_Operating_Cash).all()
    #
    # def get_public_debt_transactions(self):
    #     with self.session_factory() as session:
    #         return session.query(Public_Debt_Transactions).all()
    #
    # def get_adjustment_public_debt_transactions_cash_basis(self):
    #     with self.session_factory() as session:
    #         return session.query(Adjustment_Public_Debt_Transactions_Cash_Basis).all()
    #
    # def get_debt_subject_to_limit(self):
    #     with self.session_factory() as session:
    #         return session.query(Debt_Subject_To_Limit).all()
    #
    # def get_inter_agency_tax_transfers(self):
    #     with self.session_factory() as session:
    #         return session.query(Inter_Agency_Tax_Transfers).all()
    #
    # def get_federal_tax_deposits(self):
    #     with self.session_factory() as session:
    #         return session.query(Federal_Tax_Deposits).all()
    #
    # def get_short_term_cash_investments(self):
    #     with self.session_factory() as session:
    #         return session.query(Short_Term_Cash_Investments).all()
    #
    # def get_income_tax_refunds_issued(self):
    #     with self.session_factory() as session:
    #         return session.query(Income_Tax_Refunds_Issued).all()
