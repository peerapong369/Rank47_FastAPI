from tkinter.tix import COLUMN
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from datetime import datetime, timedelta

from models.RankData47.rankdata47_model import DbRankData47, RankDataBase


def create(db: Session, request: RankDataBase):
    new_rankdata = DbRankData47(
        product=request.product, 
        lot=request.lot,
        W1=request.W1,
        W2=request.W2,
        L1=request.L1,
        L2=request.L2,
        SQR1=request.SQR1,
        SQR2=request.SQR2,
        SQR3=request.SQR3,
        SQR4=request.SQR4,
        SQR5=request.SQR5,
        SQR6=request.SQR6,
        SQR7=request.SQR7,
        SQR8=request.SQR8,
        ST1=request.ST1,
        ST2=request.ST2,
        ST3=request.ST3,
        ST4=request.ST4,
        result=request.result
    )
    db.add(new_rankdata)
    db.commit()
    db.refresh(new_rankdata)
    return new_rankdata


def delete(db: Session, id: int):
    sensor = db.query(DbRankData47).filter(DbRankData47.id == id).first()
    db.delete(sensor)
    db.commit()
    return JSONResponse(content={"detail": f"Sensor id {id} deleted"})



def read_rankdata47(db: Session):
    return db.query(DbRankData47).all()



def read_rankdata47_last(db: Session, start: str, end: str):
    NOW = datetime.utcnow()
    return db.query(DbRankData47).filter(DbRankData47.created_date.between(start, end)).all()

 
def read_rankdata47_by_id(db: Session, id: int):
    return db.query(DbRankData47).filter(DbRankData47.id == id).first()

def product_group(db: Session):
    return db.query(DbRankData47).group_by(DbRankData47.product).all()

def productlot_group(db: Session, product:str):
    return db.query(DbRankData47).filter(DbRankData47.product==product).group_by(DbRankData47.lot).all()

def databygroup_lot(db: Session, product:str, lot:str):
    return db.query(DbRankData47).filter(DbRankData47.product==product and DbRankData47.lot==lot).all()