from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.Hole.hole_models import HoleDataBase, HoleDataDisplayBase

from routers.holedata import holedata_controller

router = APIRouter(prefix="/holedata47", tags=["holedata47"])


@router.get("/", response_model=List[HoleDataDisplayBase])
def get_all_rankdata(db: Session = Depends(get_db)):
    return holedata_controller.read_holedata47(db)



@router.get("/last_start{start}:end{end}", response_model=List[HoleDataDisplayBase])
def get_last_rankdata(start: str, end: str, db: Session = Depends(get_db)):
    return holedata_controller.read_holedata47_last(db, start, end)


@router.get("/{id}")
def rankdata_by_id(id: int, db:Session=Depends(get_db)):
    return holedata_controller.read_holedata47_by_id(db, id)




@router.post("/")
def create_rankdata(request: HoleDataBase, db: Session = Depends(get_db)):
    return holedata_controller.create(db, request)


@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return holedata_controller.delete(db, id)


