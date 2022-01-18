from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Prometno_dovoljenje(BaseModel):
    st_vpisa: str
    datum_registracije: str


class Vozilo(BaseModel):
    tip: str
    letnica: int


class Registracija_model(BaseModel):
    id: Optional[str]
    registracijska_st: Optional[str] = None
    prometno_dovoljenje: Optional[Prometno_dovoljenje] = None
    vozilo: Optional[Vozilo] = None
    datum_osnutka: Optional[datetime] = None
    opravljena_registracija: Optional[bool] = None
    lastnik: str
