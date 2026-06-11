import sqlite3
import httpx 

class AuthRepo():
    def __init__(self, api_client: httpx.Client, local_db: sqlite3.Connection):
        self.api_client = api_client
        self.local_db = local_db

    def login(self, username: str, password: str):
        print(username, password)

    def logout(self):
        pass

    def refresh(self):
        pass

    def save_token(self):
        pass


