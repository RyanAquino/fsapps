from datetime import datetime, timedelta, timezone

from dependency_injector import providers
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.exc import IntegrityError

from api.src.models.requests.user_token import RegisterUserRequest
from api.src.models.response.user_token import TokenResponse, UserToken
from api.src.repositories.user_repository import UserNotFoundError, UserRepository
from api.src.schemas.schemas import UserDBSchema


class UserService:
    def __init__(
        self,
        user_repository: UserRepository,
        config: providers.Configuration,
        pwd_context,
        user_schema: UserDBSchema,
    ):
        self._repository = user_repository
        self.config = config
        self.pwd_context = pwd_context
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
        user_schema = self.user_schema.model_validate(user)

        return user_schema

    def login_user(self, request_payload: OAuth2PasswordRequestForm) -> TokenResponse:
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

        user_token_data = UserToken(
            sub=user.username,
            exp=datetime.now(timezone.utc)
            + timedelta(minutes=self.config.get("token_exp_minutes")),
            iat=datetime.now(timezone.utc),
        )
        encoded_jwt = jwt.encode(
            user_token_data.model_dump(),
            self.config.get("jwt_secret_key"),
            algorithm=self.config.get("jwt_algorithm"),
        )

        return TokenResponse(access_token=encoded_jwt)
