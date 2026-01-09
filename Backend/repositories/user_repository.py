# repositories/user_repository.py
from sqlalchemy.orm import Session
from database.tables import UserTable


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_login(self, login: str) -> UserTable | None:
        return (
            self.db
            .query(UserTable)
            .filter(UserTable.login == login)
            .first()
        )