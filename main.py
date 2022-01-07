from enum import Enum
import uvicorn
from fastapi import FastAPI, Depends, Response, status
from fastapi.security import HTTPBearer
import fastapi
from fastapi.middleware.cors import CORSMiddleware
from utils import VerifyToken

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
@app.get("/osnutek/{id_osnutek}")
def get_osnutek():
    return {"message": "en osnutek"}


# get osnutki_all


@app.get("/osnutek")
def get_osnutekAll(response: Response, token: str = Depends(token_auth_scheme)):
    token_val = token
    print(token_val)
    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    return {"message": "vsi osnutki"}


# post: dodaj_osnutek_registracije


@app.post("/osnutek")
def add_osnutek():
    return {"message": "hey sua"}


# put: uredi osnutek


@app.put("/osnutek/{id}")
def update_osnutek():
    return {"message": "hey sua"}


# delete: odstrani_osnutek


@app.delete("/osnutek/{id}")
def delete_osnutek():
    return {"message": "hey sua"}


# post: opravi regisrtacijo-> pošlji registracijo


@app.post("/osnutek/{id}/registracija")
def potrdi_narocilo():
    return {"message": "hey sua"}


# get: get_prejsne_registracije

# TODO need to save user id_s or mails or something
@app.post("/registracije/{user_id}")
def opravi_registracijo():
    return {"message": "hey sua"}


# get: estimiraj_strosek_registracije
@app.get("/osnutek/")
def potek_registracije():
    return {
        "potek": "Potrebujemo, vozniško dovoljenje, prometno dovoljenje in osebni dokument"
    }


@app.get("/items/{value}")
def read_item(value: Names):
    return {"Vpisali ste": value}
