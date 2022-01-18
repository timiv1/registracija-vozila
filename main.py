from enum import Enum
from pickle import NONE
from typing import Dict, Optional
import uvicorn
from fastapi import FastAPI, Depends, Response, status
from fastapi.security import HTTPBearer
import fastapi
from fastapi.middleware.cors import CORSMiddleware
from models import Registracija_model
from utils import VerifyToken
# from models import Registracija_model
from database import *
from fastapi.encoders import jsonable_encoder
app = FastAPI()
token_auth_scheme = HTTPBearer()


origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# uvicorn.run(app, host="0.0.0.0", port=8000)


class Names(str, Enum):
    value1 = "deset"
    value2 = "dvajset"
    value3 = "tridest"


# get: osnutek_registracije
@app.get("/osnutek/{id}")
async def get_osnutek(id: str):
    reg = await get_one_registracija(id)
    print(reg)
    return {"registracija": reg}


# get: osnutki_all sdas
@app.get("/osnutek")
async def get_osnutek_all(response: Response, token: str = Depends(token_auth_scheme)):
    token_val = token
    print(token_val)
    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    osnutki = await get_all_osnutek()
    if osnutki:
        return {"message": osnutki}


# post: dodaj_osnutek_registracije
@app.post("/osnutek")
async def add_osnutek(osnutek: Registracija_model):
    osnutek = jsonable_encoder(osnutek)
    result = await create_osnutek(osnutek)
    if result:
        return {"message": result}


# put: uredi osnutek
@app.put("/osnutek")
async def update_osnutek(osnutek: Registracija_model):
    osnutek = jsonable_encoder(osnutek)
    updated = await update_osnutek_by_id(osnutek)
    if updated:
        return {"message": updated}


# delete: odstrani_osnutek
@app.delete("/osnutek/{id}")
def delete_osnutek(id: str):
    return {"message": "hey sua"}


# post: opravi registracijo-> pošlji registracijo
@app.post("/osnutek/{id}/registracija")
async def potrdi_narocilo(id: str):
    result = await confirm_osnutek(id)
    if result:
        return {"message": result}


# get: estimiraj_strosek_registracije
@app.get("/registracije/")
async def get_registracije():
    registracija = await get_all_registracije()
    return {
        "message": registracija
    }


@app.get('osnutek/{user_id}')
def get_past_registracije(user_id: str):
    return{"message": "reg"}

# @app.get("/items/{value}")
# def read_item(value: Names):
#     return {"Vpisali ste": value}
