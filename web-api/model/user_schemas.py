from typing import Optional
from pydantic import BaseModel
from model.models import trendEnum

class UserDisplayBase(BaseModel):
    id: int
    username: str
    alcohol: float


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    weight: int
    resistance: int

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    id: int
    username: Optional[str] = None
    img: Optional[str] = None
    weight: Optional[int] = None
    resistance: Optional[int] = None
    alcohol: Optional[float] = None
    trend: Optional[trendEnum] = None

    class Config:
        orm_mode = True       

class UserList(UserDisplayBase):
    img: Optional[str] = None
    trend: trendEnum

    class Config:
        orm_mode = True

class UserInfo(UserList):
    weight: int
    resistance: int
