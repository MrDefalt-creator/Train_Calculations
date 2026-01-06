from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    DATABASE_URL: str = "postgresql+psycopg://user:password@localhost:5433/train_db"

    DB_HOST: Optional[str] = "localhost"
    DB_PORT: Optional[str] = "5433"
    DB_USER: Optional[str] = "postgres"
    DB_PASSWORD: Optional[str] = "root"
    DB_NAME: Optional[str] = "train_db"

    @property
    def database_url(self) -> str:
        if all([self.DB_HOST, self.DB_PORT, self.DB_USER, self.DB_PASSWORD, self.DB_NAME]):
            return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return self.DATABASE_URL
    
settings = Settings()