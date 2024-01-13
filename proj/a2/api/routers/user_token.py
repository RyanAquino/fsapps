import datetime
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from jose import jwt
from sqlalchemy.orm import Session

from api.config import settings
from api.crud.user_operations import UserOperations
from api.models.requests.user_token import UserTokenRequest
from api.schemas.schemas import Token
from api.user_dependencies import init_db

router = APIRouter()


@router.post("/login", response_model=Token)
def login_for_access_token(
    request_payload: UserTokenRequest, db: Session = Depends(init_db)
):
    """Create an access token for the verified logged-in user"""
    user_operations = UserOperations(db)
    user = user_operations.get_request_user(request_payload.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    if not user_operations.pwd_context.verify(
        request_payload.password, user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    payload = {
        "id": user.id,
        "username": user.username,
        "is_enabled": user.is_enabled,
        "exp": datetime.datetime.now(datetime.timezone.utc)
        + timedelta(minutes=settings.access_token_expire_minutes),
    }
    encoded_jwt = jwt.encode(payload, settings.secret_key, algorithm="HS256")

    return Token(access_token=encoded_jwt)
