from datetime import datetime, timedelta, timezone

from dependency_injector import providers
from fastapi import HTTPException, status
from jose import jwt
from sqlalchemy.exc import IntegrityError

from api.models.requests.user_token import LoginTokenRequest, RegisterUserRequest
from api.models.response.user_token import TokenResponse
from api.repositories.user_repository import UserNotFoundError, UserRepository
from api.schemas.schemas import UserDBSchema


class UserService:
    def __init__(
        self,
        user_repository: UserRepository,
        config: providers.Configuration,
        pwd_context,
        oauth2_scheme,
        user_schema: UserDBSchema,
    ):
        self._repository = user_repository
        self.config = config
        self.pwd_context = pwd_context
        self.oauth2_scheme = oauth2_scheme
        self.user_schema = user_schema

    def register_user(self, request_payload: RegisterUserRequest) -> UserDBSchema:
        hashed_pw = self.pwd_context.hash(request_payload.password)
        try:
            user = self._repository.add(
                username=request_payload.username, password=hashed_pw
            )
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User {request_payload.username} already exists.",
            )
        user_schema = self.user_schema.from_orm(user)

        return user_schema

    def login_user(self, request_payload: LoginTokenRequest) -> TokenResponse:
        try:
            user = self._repository.get_by_username(request_payload.username)
        except UserNotFoundError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User {request_payload.username} not found.",
            )

        if not self.pwd_context.verify(request_payload.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        user_schema = self.user_schema.from_orm(user)
        user_schema.exp = datetime.now(timezone.utc) + timedelta(
            minutes=self.config.get("token_exp_minutes")
        )
        user = user_schema.dict()
        encoded_jwt = jwt.encode(user, self.config.get("secret_key"), algorithm="HS256")

        return TokenResponse(access_token=encoded_jwt)
