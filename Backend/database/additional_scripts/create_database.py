from sqlalchemy.orm import Session
from pwdlib import PasswordHash
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
            password_hasher = PasswordHash.recommended()
            hashed_password = password_hasher.hash("admin")
            admin = UserTable(login="admin", password=hashed_password, admin_rights=True)
            session.add(admin)
            session.commit()
            session.close()


if __name__ == "__main__":
    create_tables()
    create_admin()