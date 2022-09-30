from cProfile import label
from tkinter.tix import COLUMN
from unittest import result
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from datetime import datetime, timedelta

from models.RankData47.verify_model import DbVerifyData, VerifyDataBase


def create(db: Session, request: DbVerifyData):
    new_verifydata = DbVerifyData(
        product=request.product,
        lot=request.lot,
        sheet=request.sheet,
        repW1=request.repW1,
        repW2=request.repW2,
        repL1=request.repL1,
        repL2=request.repL2, 
    )
    db.add(new_verifydata)
    db.commit()
    db.refresh(new_verifydata)
    return new_verifydata


def delete(db: Session, id: int):
    verifydata = db.query(DbVerifyData).filter(DbVerifyData.id == id).first()
    db.delete(verifydata)
    db.commit()
    return JSONResponse(content={"detail": f"Sensor id {id} deleted"})



def read_verifydata(db: Session):
    return db.query(DbVerifyData).all()



def read_verifydata_last(db: Session, start: str, end: str):
    NOW = datetime.utcnow()
    return db.query(DbVerifyData).filter(DbVerifyData.created_date.between(start, end)).all()

 
def read_verifydata_by_id(db: Session, id: int):
    return db.query(DbVerifyData).filter(DbVerifyData.id == id).first()

def product_group(db: Session):
    return db.query(
            DbVerifyData.product.label('product'),
        ).group_by(
            DbVerifyData.product
        ).all()

def lot_group(db: Session, product:str):
    return db.query(
            DbVerifyData.lot.label('lot'),
        ).filter(
            DbVerifyData.product==product
        ).group_by(
            DbVerifyData.verifylot
        ).all()


def readby_lot(db: Session, product:str, lot:int):
    return db.query(
        DbVerifyData
    ).filter(
        DbVerifyData.product==product
    ).filter(
        DbVerifyData.lot==lot
    ).all()