from pydantic import BaseModel


class UserDBSchema(BaseModel):
    id: int
    username: str
    is_active: bool

    class Config:
        from_attributes = True
        extra = "allow"
