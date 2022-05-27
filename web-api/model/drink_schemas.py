from typing import Optional
from pydantic import BaseModel
from sqlalchemy import DateTime

class DrinkDisplayBase(BaseModel):
    quantity: float
    date: DateTime

class DrinksHistory(DrinkDisplayBase):

    class Config:
        orm_mode = True

class DrinkInfo(DrinkDisplayBase):

    class Config:
        orm_mode = True

class DrinkCreate():
    uid: int
    aid: int
    quantity: float
    date: DateTime

    class Config:
        orm_mode = True

class DrinkUpdate():
    id: int
    uid: int
    aid: Optional[int] = None
    quantity: Optional[float] = None
    date: Optional[DateTime] = None
    
    class Config:
        orm_mode = True