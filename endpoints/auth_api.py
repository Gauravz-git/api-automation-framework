from core.api_client import APIClient


class AuthAPI:

    def __init__(self):
        self.client = APIClient()

    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        return self.client.post("/login", payload=payload)