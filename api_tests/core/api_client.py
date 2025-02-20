from typing import Optional, Dict, Any

import requests

from api_tests.core.config import Config


class ApiClient:
    def __init__(self, config: Config):
        self.base_url = config.BASE_URL
        self.session = requests.Session()
        self.default_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None) -> requests.Response:
        url = f"{self.base_url}/{endpoint}"
        merged_headers = {**self.default_headers, **(headers or {})}
        return self.session.get(url, params=params, headers=merged_headers)

    def post(self, endpoint: str, json: Optional[Dict[str, Any]] = None,
             headers: Optional[Dict[str, str]] = None) -> requests.Response:
        url = f"{self.base_url}/{endpoint}"
        merged_headers = {**self.default_headers, **(headers or {})}
        return self.session.post(url, json=json, headers=merged_headers)
