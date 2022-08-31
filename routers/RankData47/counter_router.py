from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.RankData47.counter_model import CounterBase, CounterDisplayBase

from routers.RankData47 import counter_controller
from utils.oauth2 import access_user_token

router = APIRouter(prefix="/counter", tags=["counter"])


@router.get("/", response_model=List[CounterDisplayBase])
def get_all_rankdata(db: Session = Depends(get_db)):
    return counter_controller.read_rankcounter(db)


@router.post("/")
def create_rankdata(request: CounterBase, db: Session = Depends(get_db)):
    return counter_controller.create(db, request)


@router.put("/{id}")
def put_api(id: int, request:CounterBase, db:Session=Depends(get_db)):
    return counter_controller.update(db, id, request)