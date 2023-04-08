from audioop import lin2adpcm
from turtle import st
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL, FLOAT
from sqlalchemy.sql import func
from datetime import datetime

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel

class DbRankData47Hole(Base):
    __tablename__ = "RankData47Hole"
    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, unique=False)
    lot = Column(String, unique=False)
    holecount = Column(Integer, unique=False)
    angleAv = Column(FLOAT, unique=False)
    angleSD = Column(FLOAT, unique=False)
    angle25 = Column(FLOAT, unique=False)
    angle75 = Column(FLOAT, unique=False)
    angleMax = Column(FLOAT, unique=False)
    angleMin = Column(FLOAT, unique=False)
    angleNGMax = Column(FLOAT, unique=False)
    NGpositionX = Column(FLOAT, unique=False)
    NGpositionY = Column(FLOAT, unique=False)
    NGfilename = Column(String, unique=False)
    OK = Column(Integer, unique=False)
    NG = Column(Integer, unique=False)
    speed = Column(FLOAT, unique=False)
    created_date = Column(DateTime, default=datetime.now)
    update_date = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

class HoleDataBase(BaseModel):
    product: str
    lot: str
    holecount: int
    angleAv : float
    angleSD : float
    angle25 : float
    angle75 : float
    angleMax : float
    angleMin : float
    angleNGMax : float
    NGpositionX : float
    NGpositionY : float
    NGfilename : str
    OK : int
    NG : int
    speed : float


class HoleDataDisplayBase(BaseModel):
    id: int
    product: str
    lot: str
    holecount: int
    angleAv : float
    angleSD : float
    angle25 : float
    angle75 : float
    angleMax : float
    angleMin : float
    angleNGMax : float
    NGpositionX : float
    NGpositionY : float
    NGfilename : str
    OK : int
    NG : int
    speed : float
    created_date: datetime
    update_date: datetime

    class Config:
        orm_mode = True


class ProductGroupDisplay(BaseModel):
    product: str

    class Config:
        orm_mode = True

class ProductLotDisplay(BaseModel):
    lot: str

    class Config:
        orm_mode = True

