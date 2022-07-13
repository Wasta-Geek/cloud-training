from fastapi import APIRouter

from database.MongoDBClient import MongoDBClient

router = APIRouter()

client = MongoDBClient()


@router.get("/users", tags=["users"])
async def get_users():
    db = await client.get_database('users')
    if db is None:
        print("ERROR")
        return ""
    return await client.list_collection_names(db)
