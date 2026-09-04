import enum
import uuid

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class MovieGenreEnum(str, enum.Enum):
    COMEDY = "COMEDY"
    ACTION = "ACTION"
    ADVENTURE = "ADVENTURE"
    DOCUMENTRY = "DOCUMENTRY"
    ROMANTIC = "ROMANTIC"
    SCIFI = "SCI-FI"


class EventGEnreEnum(str, enum.Enum):
    COMEDY = "COMEDY"
    MUSIC = "MUSIC"
    DANCE = "DANCE"
    EDUCATION = "EDUCATION"

class SeatTypeEnum(str, enum.Enum):
    NORMAL = "NORMAL"
    PREMIUM = "PREMINUM"
    RECLINER = "RECLINER"
    FANZONE = "FANZONE"
    
class StatusEnum(str, enum.Enum):
    AVAILABLE = "AVAILABLE"
    BOOKED = "BOOKED"


class MovieModel(Model):
    __table_name__ = "movies"

    movie_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    title = columns.Text()
    description = columns.Text()
    language = columns.Text()
    duration_minutes = columns.Integer()
    release_date = columns.Date()
    genre = columns.Text(default=MovieGenreEnum.COMEDY.value)
    created_at = columns.DateTime()


class EventModel(Model):
    __table_name__ = "events"

    event_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    title = columns.Text()
    description = columns.Text()
    date = columns.Date()
    genre = columns.Text(default=MovieGenreEnum.COMEDY.value)
    duration_minutes = columns.Integer()
    create_at = columns.DateTime()


class VenueModel(Model):
    __table_name__ = "venues"

    venue_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    name = columns.Text()
    city = columns.Text()
    address = columns.Text()
    total_screen = columns.Integer()
    geo_location = columns.Text()


class ShowByMovieModel(Model):
    __table_name__ = "show_by_movie"

    movie_id = columns.UUID(primary_key=True, partition_key=True)
    city = columns.Text()
    show_time = columns.DateTime(primary_key=True, clustering_order="ASC")

    show_id = columns.UUID()
    venue_id = columns.UUID()
    venune_name = columns.Text()
    screen_name = columns.Text()


class ShowByEventModel(Model):
    __table_name__ = "show_by_event"

    event_id = columns.UUID(primary_key=True, partition_key=True)
    city = columns.Text()
    show_time = columns.DateTime(primary_key=True, clustering_order="ASC")

    show_id = columns.UUID()
    venue_id = columns.UUID()
    venue_name = columns.Text()
    
class ShowModel(Model):
    __table_name__ = "shows"

    show_id = columns.UUID(primary_key=True)
    movie_id = columns.UUID()
    venue_id = columns.UUID()
    screen_name = columns.Text()
    show_time = columns.DateTime()
    is_active = columns.Boolean(default=True)

class SeatsByShowModel(Model):
    __table_name__ = "seat_by_show"

    show_id = columns.UUID(primary_key=True, partition_key=True)
    seat_id = columns.Text(primary_key=True)

    row_name = columns.Text()
    seat_type = columns.Text(default=SeatTypeEnum.NORMAL.value)
    price = columns.Decimal()
    status = columns.Text(default=StatusEnum.AVAILABLE.value)