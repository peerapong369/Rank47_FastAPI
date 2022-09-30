from cProfile import label
from tkinter.tix import COLUMN
from unittest import result
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from datetime import datetime, timedelta

from models.RankData47.verifylot_model import DbVerifyLotData, VerifyLotDataBase


def createverifylot(db: Session, request: DbVerifyLotData):
    new_verifylotdata = DbVerifyLotData(
        product=request.product,
        lot=request.lot,
        lotdataid=request.lotdataid 
    )
    db.add(new_verifylotdata)
    db.commit()
    db.refresh(new_verifylotdata)
    return new_verifylotdata



def read_verifylotdata_by_id(db: Session, id: str):
    return db.query(DbVerifyLotData).filter(DbVerifyLotData.lotdataid == id).all()