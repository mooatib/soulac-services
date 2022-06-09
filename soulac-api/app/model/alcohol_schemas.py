from typing import Optional
from pydantic import BaseModel

class AlcoholDisplayBase(BaseModel):
    id: int
    name: str
    type: bool
    percentage: float
    
    class Config:
        orm_mode = True

class AlcoholList(AlcoholDisplayBase):
    id: int
    class Config:
        orm_mode = True 

class AlcoholCreate(BaseModel):
    name: str
    type: bool
    percentage: float
    class Config:
        orm_mode = True

class AlcoholUpdate(BaseModel):
    id: int
    name: Optional[str]
    type: Optional[bool]
    percentage: Optional[float]
    
    class Config:
        orm_mode = True