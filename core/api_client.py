import requests
from utils.config import BASE_URL, TIMEOUT, DEFAULT_HEADERS
from utils.logger import get_logger

logger = get_logger()


class APIClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)  # 🔥 Important

    def get(self, endpoint, headers=None, params=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET Request → {url}")
        response = self.session.get(
            url,
            headers=headers,
            params=params,
            timeout=TIMEOUT
        )
        logger.info(f"Response Status → {response.status_code}")
        return response

    def post(self, endpoint, payload=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST Request → {url}")
        logger.info(f"Payload → {payload}")
        response = self.session.post(
            url,
            json=payload,
            headers=headers,
            timeout=TIMEOUT
        )
        logger.info(f"Response Status → {response.status_code}")
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE Request → {url}")
        response = self.session.delete(
            url,
            headers=headers,
            timeout=TIMEOUT
        )
        logger.info(f"Response Status → {response.status_code}")
        return response