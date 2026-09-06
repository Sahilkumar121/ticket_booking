from async_cassandra import AsyncCluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from core.config import setting
from models.cassandra_model import (
    EventModel,
    MovieModel,
    SeatsByShowModel,
    ShowByEventModel,
    ShowByMovieModel,
    ShowModel,
    VenueModel,
)


class CassandraDB:
    def __init__(self) -> None:
        self.cluster: AsyncCluster | None = None
        self.session = None

    async def connect(self):

        self.cluster = AsyncCluster(
            contact_points=[setting.contact_points],
            port=setting.cassandra_port,
            protocol_version=5,
        )

        self.session = await self.cluster.connect("ticket_booking")

        # sync function runs on startup
        connection.setup(
            hosts=[setting.contact_points],
            default_keyspace="ticket_booking",
            port=setting.cassandra_port,
            protocol_version=5,
        )

        # Automaticaly create table if they do not exist
        sync_table(MovieModel)
        sync_table(EventModel)
        sync_table(VenueModel)
        sync_table(ShowByMovieModel)
        sync_table(ShowByEventModel)
        sync_table(ShowModel)
        sync_table(SeatsByShowModel)

    async def disconnect(self):
        if self.session:
            await self.session.close()
        if self.cluster:
            await self.cluster.shutdown()


cassandra_db = CassandraDB()
