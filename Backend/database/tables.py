from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, as_declarative, mapped_column


@as_declarative()
class AbstractModel:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)

class UserTable(AbstractModel):
    __tablename__ = "users"

    login: Mapped[str] = mapped_column(String(200), index=True, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    admin_rights: Mapped[bool] = mapped_column(default=False, nullable=False)

class StationTable(AbstractModel):
    __tablename__ = "stations"

    name: Mapped[str] = mapped_column(String(200), index=True, unique=True, nullable=False)

class RouteTable(AbstractModel):
    __tablename__ = "routes"

    from_station: Mapped[int] = mapped_column(Integer, ForeignKey('stations.id'), nullable=False,)
    to_station: Mapped[int] = mapped_column(Integer, ForeignKey('stations.id'), nullable=False)
    distance: Mapped[int] = mapped_column( nullable=False)
    travel_time: Mapped[int] = mapped_column(nullable=False)
