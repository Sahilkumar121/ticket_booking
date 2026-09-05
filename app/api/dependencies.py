from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.cassandra_db import cassandra_db
from app.db.postgre_db import asyncLocalSession


async def get_db():
    async with asyncLocalSession.begin() as session:
        yield session


async def get_cassandra_db():
    if cassandra_db.session is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Cassandra DB is not Connected",
        )
    yield cassandra_db.session


postgre_session = Annotated[Session, Depends(get_db)]
cassandra_session = Annotated[Session, Depends(get_cassandra_db)]
