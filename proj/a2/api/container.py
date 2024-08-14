from dependency_injector import containers, providers
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from api.database import Database
from api.repositories.operating_cash_balance_repository import (
    OperatingCashBalanceRepository,
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
            "operating_cash_balance": repositories.operating_cash_balance_repository
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
