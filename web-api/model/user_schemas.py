from typing import Optional
from pydantic import BaseModel
from model.models import trendEnum

class UserDisplayBase(BaseModel):
    id: int
    img: Optional[str] = None

class UserList(UserDisplayBase):
    alcohol: float
    username: str
    trend: trendEnum

    class Config:
        orm_mode = True

class UserInfo(UserList):
    weight: int
    resistance: int

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

