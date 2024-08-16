from typing import Callable, Optional

from api.src.repositories.dts_tables_repository import DTSTablesBaseRepository
from api.src.services.adjustment_public_debt_transactions_cash_basis_service import (
    AdjustmentPublicDebtTransactionsCashBasisService,
)
from api.src.services.debt_subject_to_limit_service import DebtSubjectToLimitService
from api.src.services.deposits_withdrawals_operating_cash_service import (
    DepositsWithdrawalsOperatingCashBalanceService,
)
from api.src.services.federal_tax_deposits_service import FederalTaxDepositsService
from api.src.services.income_tax_refunds_issued_service import (
    IncomeTaxRefundsIssuedService,
)
from api.src.services.inter_agency_tax_transfers_service import (
    InterAgencyTaxTransfersService,
)
from api.src.services.operating_cash_balance_service import OperatingCashBalanceService
from api.src.services.public_debt_transactions_service import (
    PublicDebtTransactionsService,
)
from api.src.services.short_term_cash_investments_service import (
    ShortTermCashInvestmentsService,
)


class DTSTablesService:
    def __init__(self, dts_tables_repository: dict[str, DTSTablesBaseRepository]):
        self._repository = dts_tables_repository

    def get_repository(self, table_name: str) -> DTSTablesBaseRepository:
        repository: Optional[Callable] = self._repository.get(table_name)

        if not repository:
            raise InvalidTable

        return repository()

    def get_service(self, table_name: str):
        repository = self.get_repository(table_name)
        table_service_mappings = {
            "operating_cash_balance": OperatingCashBalanceService,
            "adjustment_public_debt_transactions_cash_basis": AdjustmentPublicDebtTransactionsCashBasisService,
            "debt_subject_to_limit": DebtSubjectToLimitService,
            "deposits_withdrawals_operating_cash_balance": DepositsWithdrawalsOperatingCashBalanceService,
            "federal_tax_deposits": FederalTaxDepositsService,
            "income_tax_refunds_issued": IncomeTaxRefundsIssuedService,
            "inter_agency_tax_transfers": InterAgencyTaxTransfersService,
            "public_debt_transactions": PublicDebtTransactionsService,
            "short_term_cash_investments": ShortTermCashInvestmentsService,
        }
        service = table_service_mappings.get(table_name)

        return service(repository, service)

    def get_data(self, table_name, filters=None):
        service = self.get_service(table_name)
        data = service.get_data(filters)
        return data


class InvalidTable(Exception):
    def __init__(self, table_name):
        super().__init__(f"Invalid table name: {table_name}")
