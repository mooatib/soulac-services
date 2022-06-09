from typing import Optional
from pydantic import BaseModel
from ..model.models import trendEnum
from .user_schemas import User


class SoulacaisBase(BaseModel):
    id: int
    user: User
    
    class Config:
        orm_mode = True


class SoulacaisDisplayBase(SoulacaisBase):
    img: Optional[str] = None


class SoulacaisList(SoulacaisDisplayBase):
    alcohol: float
    trend: trendEnum

    class Config:
        orm_mode = True


class SoulacaisInfo(SoulacaisList):
    weight: int
    resistance: int


class SoulacaisCreate(BaseModel):
    user: User
    weight: int
    resistance: int

    class Config:
        orm_mode = True


class SoulacaisUpdate(BaseModel):
    id: Optional[int] = None
    user: Optional[User] = None
    img: Optional[str] = None
    sex: Optional[bool] = None
    weight: Optional[int] = None
    resistance: Optional[int] = None
    alcohol: Optional[float] = None
    trend: Optional[trendEnum] = None
    class Config:
        orm_mode = True
