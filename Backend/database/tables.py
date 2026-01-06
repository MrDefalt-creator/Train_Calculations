from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table

from database.database import metadata

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement="auto", nullable=False),
    Column("login", String(200), index=True, unique=True, nullable=False),
    Column("password", String(200), nullable=False),
    Column("admin_rights", Boolean, default=False, nullable=False)
)

stations_table = Table(
    "stations",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement="auto", nullable=False),
    Column("name", String(200), index=True, unique=True, nullable=False),
)

routes_table = Table(
    "routes",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("from_station", Integer, ForeignKey(column='stations.id'), nullable=False,),
    Column("to_station", Integer, ForeignKey(column='stations.id'), nullable=False),
    Column("distance", Integer, nullable=False),
    Column("travel_time", Integer, nullable=False)
)
