from fastapi import FastAPI

from models.database import engine
# #from models.inventory import inventory_model
# #from models.users import users_model
from models.Hole import hole_models
# from models.RankData47 import rankdata47_model, counter_model, verify_model, verifylot_model
# from models.Machine import machine_model


# #from routers.inventory import inventory_rounter
# #from routers.users import user_router
# #from routers.auth import authen_router
from routers.holedata import holedata_router
# from routers.RankData47 import rankdata47_router, counter_router, verify_router, verifylot_router
# from routers.machine import machineavailable_router



app = FastAPI()
# #app.include_router(authen_router.router)
# #app.include_router(inventory_rounter.router)
# #app.include_router(user_router.router)
# app.include_router(sensor_rounter.router)
# app.include_router(rankdata47_router.router)
# app.include_router(counter_router.router)
# app.include_router(verify_router.router)
# app.include_router(verifylot_router.router)
# app.include_router(machineavailable_router.router)
app.include_router(holedata_router.router)



@app.get("/")
def hello():
    return {"hellow": "Fast-API"}


#inventory_model.Base.metadata.create_all(engine)
#users_model.Base.metadata.create_all(engine)
hole_models.Base.metadata.create_all(engine)
# rankdata47_model.Base.metadata.create_all(engine)
# counter_model.Base.metadata.create_all(engine)
# verify_model.Base.metadata.create_all(engine)
# verifylot_model.Base.metadata.create_all(engine)
# machine_model.Base.metadata.create_all(engine)