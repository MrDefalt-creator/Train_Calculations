from database.database import engine, metadata

from .. import tables


def create_database():
    metadata.create_all(engine)

if __name__ == "__main__":
    create_database()