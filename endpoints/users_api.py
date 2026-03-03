from core.api_client import APIClient


class UsersAPI:

    def __init__(self):
        self.client = APIClient()

    def get_users(self):
        return self.client.get("/users")

    def create_user(self, name, email):
        payload = {
            "name": name,
            "email": email
        }
        return self.client.post("/users", payload=payload)

    def delete_user(self, user_id):
        return self.client.delete(f"/users/{user_id}")