import pytest
from endpoints.users_api import UsersAPI
from core.base_test import BaseTest


class TestUsers(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.users_api = UsersAPI()

    def test_get_users(self):
        response = self.users_api.get_users()

        self.validate_status_code(response, 200)

        data = response.json()

        # JSONPlaceholder returns list
        assert isinstance(data, list)
        assert len(data) > 0
        assert "id" in data[0]
        assert "name" in data[0]

    def test_create_user(self):
        response = self.users_api.create_user("Gaurav", "Automation Engineer")

        self.validate_status_code(response, 201)

        data = response.json()

        assert data["name"] == "Gaurav"
        assert data["job"] == "Automation Engineer"
        assert "id" in data