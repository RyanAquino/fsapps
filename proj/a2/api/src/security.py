from dependency_injector.wiring import Provide, inject
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import ExpiredSignatureError, JWTError, jwt

from api.src.container import Application

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


@inject
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    config=Depends(Provide[Application.config.application]),
    user_repository=Depends(Provide[Application.repositories.user_repository]),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            config.get("jwt_secret_key"),
            algorithms=[config.get("jwt_algorithm")],
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError:
        raise credentials_exception

    user = user_repository.get_by_username(username)

    if user is None:
        raise credentials_exception

    if user.is_active is False:
        raise HTTPException(status_code=400, detail="Inactive user")

    return user
