from core.user.user import User
from core.user.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def register_user(self, name, email, password):
        #if self.repository.buscar_por_email(email):
        #    raise ValueError("Usuário já cadastrado com esse e-mail.")
        user = User(name, email, password)
        return self.repository.save(user)

    def list_users(self):
        return self.repository.list_all()

    def remove_user(self, email):
        if not self.repository.search_by_email(email):
            raise ValueError("Usuário não encontrado.")
        self.repository.remove_by_email(email)

    def remove_user_by_id(self, id):
        if not self.repository.get_by_id(id):
            raise ValueError("Usuário não encontrado.")
        self.repository.remove_by_id(id)

    def get_user_by_id(self, id):
        user = self.repository.get_by_id(id)
        if user is None:
            raise ValueError("Usuário não encontrado.")
        return user


userService = UserService()
