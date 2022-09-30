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

class DbMachineAviable(Base):
    __tablename__ = "MachineTime"
    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime, default=datetime.now)
    number = Column(Integer, unique=False)
    readytime = Column(Integer, unique=False)

class MachineAvialableDataBase(BaseModel):
    number: int
    readytime: int


class ReadyTimeDisplayBase(BaseModel):
    id: int
    created_date: datetime
    number: int
    readytime: int

    class Config:
        orm_mode = True


