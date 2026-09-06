from contextlib import asynccontextmanager

from api.v1.router import route
from db.cassandra_db import cassandra_db
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    await cassandra_db.connect()

    yield

    await cassandra_db.disconnect()


app = FastAPI(title="Ticket Booking", lifespan=lifespan)


app.include_router(route)


@app.get("/")
def home():
    return {"status": "True", "messgae": "Ticket Booking System"}
