from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, login: str, password: str):
        user = self.user_repository.find_by_login(login)

        if not user:
            return None

        return user