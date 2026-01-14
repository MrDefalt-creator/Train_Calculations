from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    DATABASE_URL: str = "postgresql+psycopg://user:password@localhost:5433/train_db"

    DB_HOST: Optional[str] = "localhost"
    DB_PORT: Optional[str] = "5433"
    DB_USER: Optional[str] = "postgres"
    DB_PASSWORD: Optional[str] = "root"
    DB_NAME: Optional[str] = "train_db"

    SECRET_KEY_ACCESS: Optional[str] = "170b45bc27972f7ddbf40919a2f747712370c1747f39246e95178e06d2a6cbd1"
    SECRET_KEY_REFRESH: Optional[str] = "b593e308abc68289966041037a603700f2d5ba466095c66b07085692de2efb2c"
    ALGORITHM: Optional[str] = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int] = 30
    REFRESH_TOKEN_EXPIRE_DAYS: Optional[int] = 30

    @property
    def database_url(self) -> str:
        if all([self.DB_HOST, self.DB_PORT, self.DB_USER, self.DB_PASSWORD, self.DB_NAME]):
            return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return self.DATABASE_URL
