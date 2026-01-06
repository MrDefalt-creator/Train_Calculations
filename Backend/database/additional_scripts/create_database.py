from sqlalchemy.orm import Session

from database.database import engine
from database.tables import AbstractModel


def create_database():
    with Session(engine) as session:
        with session.begin():
            AbstractModel.metadata.create_all(engine) 

if __name__ == "__main__":
    create_database()