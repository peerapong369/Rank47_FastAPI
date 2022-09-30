from cProfile import label
from tkinter.tix import COLUMN
from unittest import result
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from datetime import datetime, timedelta

from models.Machine.machine_model import DbMachineAviable, MachineAvialableDataBase


def create(db: Session, request: MachineAvialableDataBase):
    new_readytimedata = DbMachineAviable(
        number=request.number,
        readytime=request.readytime
    )
    db.add(new_readytimedata)
    db.commit()
    db.refresh(new_readytimedata)
    return new_readytimedata


def delete(db: Session, id: int):
    sensor = db.query(DbMachineAviable).filter(DbMachineAviable.id == id).first()
    db.delete(sensor)
    db.commit()
    return JSONResponse(content={"detail": f"Sensor id {id} deleted"})



def read_machinereadydata(db: Session):
    return db.query(DbMachineAviable).all()



def read_machinereadydata_last(db: Session, start: str, end: str):
    NOW = datetime.utcnow()
    return db.query(DbMachineAviable).filter(DbMachineAviable.created_date.between(start, end)).all()

 
def read_machinereadydata_by_id(db: Session, id: int):
    return db.query(DbMachineAviable).filter(DbMachineAviable.id == id).first()
