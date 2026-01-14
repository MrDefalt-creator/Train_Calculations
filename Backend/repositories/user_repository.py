from sqlalchemy.orm import Session
from database.tables import UserTable

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_login(self, login: str) -> UserTable | None:
        try:
            return (
                self.db
                .query(UserTable)
                .filter(UserTable.login == login)
                .first()
            )
        finally:
            self.db.close()

    def find_by_id(self, id: int) -> UserTable | None:
        try:
            return (
                self.db
                .query(UserTable)
                .filter(UserTable.id == id)
                .first()
            )
        finally:
            self.db.close()