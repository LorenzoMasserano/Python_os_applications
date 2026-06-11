from data.usecase.login_usecase import LoginUseCase

class LoginCtrl():
    
    def login(self, username: str, password: str):
        LoginUseCase().__call__(username, password)
