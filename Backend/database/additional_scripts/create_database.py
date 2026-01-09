from sqlalchemy.orm import Session
import bcrypt
from database.database import engine
from database.tables import AbstractModel, UserTable


def create_tables():
    with Session(engine) as session:
        with session.begin():
            AbstractModel.metadata.create_all(engine)
            session.commit()
            session.close()

def create_admin():
    with Session(engine) as session:
        with session.begin():
            hashed_password = bcrypt.hashpw(
                "admin".encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')
            admin = UserTable(login="admin", password=hashed_password, admin_rights=True)
            session.add(admin)
            session.close()


if __name__ == "__main__":
    create_tables()
    create_admin()