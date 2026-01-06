from sqlalchemy import create_engine, text, Connection, MetaData
from sqlalchemy.orm import Session, relationship
from core.config import settings


engine =  create_engine(
    settings.database_url,
    echo=True,
    pool_size=5,
    max_overflow=10
)


metadata = MetaData()