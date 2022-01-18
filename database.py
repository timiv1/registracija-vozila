import os
import motor.motor_asyncio
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client['registracije_db']
registracija_collection = db.get_collection('registracije')


async def get_all_registracije():
    registracije = []
    async for reg in await registracija_collection.find_one({"_id": ObjectId(id)}):
        registracije.append(convert_registracija(reg))
    return registracije


async def get_all_osnutek():
    registracije = []
    async for reg in registracija_collection.find():
        registracije.append(convert_registracija(reg))
    return registracije


async def get_one_registracija(id: str):
    registracija = await registracija_collection.find_one({"_id": ObjectId(id)})
    if registracija:
        return convert_registracija(registracija)


async def get_one_osnutek(id: str):
    registracija = await registracija_collection.find_one({"_id": ObjectId(id)})
    if registracija:
        return convert_registracija(registracija)


async def create_osnutek(payload) -> dict:
    osnutek = await registracija_collection.insert_one(payload)
    if osnutek:
        return "uspešno ste ustvarili osnutek"


async def confirm_osnutek(id) -> dict:
    print(id)
    osnutek = await registracija_collection.update_one({'_id': ObjectId(id)}, {'$set': {'opravljena_registracija': True}})
    if osnutek:
        return "uspešno ste potrdili osnutek"


async def update_osnutek_by_id(payload) -> dict:
    id = payload['id']
    payload.pop("id")
    osnutek = await registracija_collection.update_one({'_id': ObjectId(id)}, {'$set': payload})
    if osnutek:
        return "uspešno ste posodobili osnutek"

# helpers


def convert_test(payload) -> dict:
    return{"id": str(payload['_id']),
           "registracijska_st": payload['registracijska_st']
           }


def convert_registracija(payload) -> dict:
    return{
        "_id": str(payload['_id']),
        "registracijska_st": payload['registracijska_st'],
        "prometno_dovoljenje": payload['prometno_dovoljenje'],
        "vozilo": payload['vozilo'],
        "datum_osnutka": payload['datum_osnutka'],
        "opravljena_registracija": payload['opravljena_registracija'],
        "lastnik": payload["lastnik"]
    }
