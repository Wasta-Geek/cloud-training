from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pymongo.errors import ServerSelectionTimeoutError

from database.MongoDBClient import MongoDBClient
from routers import users

mongo_client = MongoDBClient()

app = FastAPI()
app.include_router(users.router)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Authorization service 2"}


@app.exception_handler(ServerSelectionTimeoutError)
async def database_timeout_exception_handler(_request: Request, _exc: ServerSelectionTimeoutError):
    return JSONResponse(
        status_code=503,
        content={
            "message": "Cannot communicate with the database (probably offline)"
        }
    )
