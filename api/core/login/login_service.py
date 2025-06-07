from core.login.login import Login
from core.login.login_repository import LoginRepository

class LoginService:
    def __init__(self):
        self.repository = LoginRepository()

    def autenticar(self, login: Login):
        user = self.repository.search_user_by_email(login.email)
        if not user:
            raise ValueError("Usuário não encontrado.")
        if user.password != login.password:
            raise ValueError("Senha incorreta.")
        return user