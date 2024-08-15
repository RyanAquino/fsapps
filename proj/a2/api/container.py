from dependency_injector import containers, providers
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from api.database import Database
from api.repositories.adjustment_public_debt_transactions_cash_basis_repository import (
    AdjustmentPublicDebtTransactionsCashBasisRepository,
)
from api.repositories.debt_subject_to_limit_repository import (
    DebtSubjectToLimitRepository,
)
from api.repositories.deposits_withdrawals_operating_cash_repository import (
    DepositsWithdrawalsOperatingCashBalanceRepository,
)
from api.repositories.federal_tax_deposits_repository import (
    FederalTaxDepositsRepository,
)
from api.repositories.income_tax_refunds_issued_repository import (
    IncomeTaxRefundsIssuedRepository,
)
from api.repositories.inter_agency_tax_transfers_repository import (
    InterAgencyTaxTransfersRepository,
)
from api.repositories.operating_cash_balance_repository import (
    OperatingCashBalanceRepository,
)
from api.repositories.public_debt_transactions_repository import (
    PublicDebtTransactionsRepository,
)
from api.repositories.short_term_cash_investments_repository import (
    ShortTermCashInvestmentsRepository,
)
from api.repositories.user_repository import UserRepository
from api.schemas.schemas import UserDBSchema
from api.services.dts_tables_service import DTSTablesService
from api.services.user_service import UserService


class Gateways(containers.DeclarativeContainer):
    config = providers.Configuration()
    db = providers.Singleton(Database, db_url=config.dsn)


class Repositories(containers.DeclarativeContainer):
    gateways = providers.DependenciesContainer()

    user_repository = providers.Factory(
        UserRepository, session_factory=gateways.db.provided.session
    )

    operating_cash_balance_repository = providers.Factory(
        OperatingCashBalanceRepository, session_factory=gateways.db.provided.session
    )
    adjustment_public_debt_transactions_cash_basis_repository = providers.Factory(
        AdjustmentPublicDebtTransactionsCashBasisRepository,
        session_factory=gateways.db.provided.session,
    )
    debt_subject_to_limit_repository = providers.Factory(
        DebtSubjectToLimitRepository, session_factory=gateways.db.provided.session
    )
    deposits_withdrawals_operating_cash_balance_repository = providers.Factory(
        DepositsWithdrawalsOperatingCashBalanceRepository,
        session_factory=gateways.db.provided.session,
    )
    federal_tax_deposits_repository = providers.Factory(
        FederalTaxDepositsRepository, session_factory=gateways.db.provided.session
    )
    income_tax_refunds_issued_repository = providers.Factory(
        IncomeTaxRefundsIssuedRepository,
        session_factory=gateways.db.provided.session,
    )
    inter_agency_tax_transfers_repository = providers.Factory(
        InterAgencyTaxTransfersRepository,
        session_factory=gateways.db.provided.session,
    )
    public_debt_transactions_repository = providers.Factory(
        PublicDebtTransactionsRepository,
        session_factory=gateways.db.provided.session,
    )
    short_term_cash_investments_repository = providers.Factory(
        ShortTermCashInvestmentsRepository,
        session_factory=gateways.db.provided.session,
    )


class Services(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()
    config = providers.Configuration()

    pwd_context = providers.Singleton(
        CryptContext, schemes=["bcrypt"], deprecated="auto"
    )

    oauth2_scheme = providers.Singleton(
        OAuth2PasswordBearer, tokenUrl="api/v1/auth/login"
    )

    user_service = providers.Factory(
        UserService,
        user_repository=repositories.user_repository,
        config=config,
        pwd_context=pwd_context,
        oauth2_scheme=oauth2_scheme,
        user_schema=UserDBSchema,
    )

    dts_tables_service = providers.Factory(
        DTSTablesService,
        dts_tables_repository={
            "operating_cash_balance": repositories.operating_cash_balance_repository,
            "adjustment_public_debt_transactions_cash_basis": repositories.adjustment_public_debt_transactions_cash_basis_repository,
            "debt_subject_to_limit": repositories.debt_subject_to_limit_repository,
            "deposits_withdrawals_operating_cash_balance": repositories.deposits_withdrawals_operating_cash_balance_repository,
            "federal_tax_deposits": repositories.federal_tax_deposits_repository,
            "income_tax_refunds_issued": repositories.income_tax_refunds_issued_repository,
            "inter_agency_tax_transfers": repositories.inter_agency_tax_transfers_repository,
            "public_debt_transactions": repositories.public_debt_transactions_repository,
            "short_term_cash_investments": repositories.short_term_cash_investments_repository,
        },
    )


class Application(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["api.endpoints"])
    config = providers.Configuration(yaml_files=["api/config.yml"])

    gateways = providers.Container(Gateways, config=config.database)
    repositories = providers.Container(Repositories, gateways=gateways)
    services = providers.Container(
        Services,
        config=config.application,
        repositories=repositories,
    )
