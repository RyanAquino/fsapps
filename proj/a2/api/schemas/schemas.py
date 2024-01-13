from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"


class TokenData(BaseModel):
    username: str or None = None


class UserBase(BaseModel):
    username: str
    is_enabled: bool or None = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    hashed_password: str

    class Config:
        from_attributes = True
