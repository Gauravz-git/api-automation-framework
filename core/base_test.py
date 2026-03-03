class BaseTest:

    def validate_status_code(self, response, expected_code):
        assert response.status_code == expected_code, \
            f"Expected {expected_code}, but got {response.status_code}"

    def validate_key_present(self, response, key):
        assert key in response.json(), \
            f"Key '{key}' not found in response"