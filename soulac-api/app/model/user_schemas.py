from pydantic import BaseModel


class UserBase(BaseModel):
    username: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    email: str
