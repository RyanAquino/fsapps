from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from api.src.container import Application
from api.src.models.requests.user_token import RegisterUserRequest
from api.src.services.user_service import UserService

router = APIRouter()

from fastapi.security import OAuth2PasswordRequestForm


@router.post("/login")
@inject
def login(
    request_payload: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    user_service: UserService = Depends(Provide[Application.services.user_service]),
):
    return user_service.login_user(request_payload)


@router.post("/register")
@inject
def register(
    request_payload: RegisterUserRequest,
    user_service: UserService = Depends(Provide[Application.services.user_service]),
):
    return user_service.register_user(request_payload)
