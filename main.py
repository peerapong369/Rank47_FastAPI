from fastapi import FastAPI

from models.database import engine
#from models.inventory import inventory_model
#from models.users import users_model
from models.sensor import sensor_model
from models.RankData47 import rankdata47_model, counter_model


#from routers.inventory import inventory_rounter
#from routers.users import user_router
#from routers.auth import authen_router
from routers.sensor import sensor_rounter
from routers.RankData47 import rankdata47_router, counter_router


app = FastAPI()
#app.include_router(authen_router.router)
#app.include_router(inventory_rounter.router)
#app.include_router(user_router.router)
app.include_router(sensor_rounter.router)
app.include_router(rankdata47_router.router)
app.include_router(counter_router.router)



@app.get("/")
def hello():
    return {"hellow": "Fast-API"}


#inventory_model.Base.metadata.create_all(engine)
#users_model.Base.metadata.create_all(engine)
sensor_model.Base.metadata.create_all(engine)
rankdata47_model.Base.metadata.create_all(engine)
counter_model.Base.metadata.create_all(engine)