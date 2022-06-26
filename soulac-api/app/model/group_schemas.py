from typing import List, Optional
from pydantic import BaseModel


class GroupBase(BaseModel):
    id: int
    name: str
    img: Optional[str] = None
    private: bool

    class Config:
        orm_mode = True


class GroupInfo(GroupBase):
    description: Optional[str] = None


class GroupCreate(GroupBase):
    description: Optional[str] = None
    private: bool


class GroupUpdate(GroupBase):
    id: int
    name: Optional[str] = None
    img: Optional[str] = None
    description: Optional[str] = None
    private: Optional[bool] = None
