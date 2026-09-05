from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.cassandra_db import cassandra_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await cassandra_db.connect()

    yield

    await cassandra_db.disconnect()


app = FastAPI(title="Ticket Booking", lifespan=lifespan)


@app.get("/")
def home():
    return {"status": "True", "messgae": "Ticket Booking System"}
