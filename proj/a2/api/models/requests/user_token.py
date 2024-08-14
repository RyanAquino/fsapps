from pydantic import BaseModel


class LoginTokenRequest(BaseModel):
    username: str
    password: str


class RegisterUserRequest(BaseModel):
    username: str
    password: str
