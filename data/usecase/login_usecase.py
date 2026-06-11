from data.repositories.auth_repo import AuthRepo
from di.di_api import container

class LoginUseCase():
    def __init__(self):
        self.auth_repository = container.resolve(AuthRepo)

    def __call__(self, username: str, password: str):
        self.auth_repository.login(username= username, password= password)
