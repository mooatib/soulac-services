from typing import List, Optional
from pydantic import BaseModel
from .user_schemas import User


class SoulacaisBase(BaseModel):
    id: int
    user: User
    img: Optional[str] = None
    role: Optional[str] = None

    class Config:
        orm_mode = True


class GroupBase(BaseModel):
    id: int
    name: str
    img: Optional[str] = None

    class Config:
        orm_mode = True


class GroupInfo(GroupBase):
    description: Optional[str] = None
    private: bool
    role: Optional[str] = None
    soulacais: List[SoulacaisBase]


class GroupCreate(GroupBase):
    description: Optional[str] = None
    private: bool


class GroupUpdate(GroupBase):
    id: int
    name: Optional[str] = None
    img: Optional[str] = None
    description: Optional[str] = None
    private: Optional[bool] = None
