from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import Settings


engine = create_engine(
    Settings.database_url,
    echo=True,
    pool_size=5,
    max_overflow=10
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
