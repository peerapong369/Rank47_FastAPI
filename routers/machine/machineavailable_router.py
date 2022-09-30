from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.Machine.machine_model import MachineAvialableDataBase, ReadyTimeDisplayBase

from routers.machine import machineavailable_controller

router = APIRouter(prefix="/machineavailable", tags=["machineavailable"])


@router.get("/", response_model=List[ReadyTimeDisplayBase])
def get_all_availabledata(db: Session = Depends(get_db)):
    return machineavailable_controller.read_machinereadydata(db)



@router.get("/last_start{start}:end{end}", response_model=List[ReadyTimeDisplayBase])
def get_last_availabledata(start: str, end: str, db: Session = Depends(get_db)):
    return machineavailable_controller.read_machinereadydata_last(db, start, end)


@router.get("/{id}")
def avaikabledata_by_id(id: int, db:Session=Depends(get_db)):
    return machineavailable_controller.read_machinereadydata_by_id(db, id)



@router.post("/")
def create_machineavailabledata(request: MachineAvialableDataBase, db: Session = Depends(get_db)):
    return machineavailable_controller.create(db, request)


@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return machineavailable_controller.delete(db, id)


