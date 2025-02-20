from typing import Optional, Dict, Any
import httpx

from api_tests.core.config import Config


class ApiClient:
    def __init__(self, config: Config):
        self.base_url = config.BASE_URL
        self.default_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.client = httpx.AsyncClient(headers=self.default_headers)

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None,
                  headers: Optional[Dict[str, str]] = None) -> httpx.Response:
        url = f"{self.base_url}/{endpoint}"
        merged_headers = {**self.default_headers, **(headers or {})}
        response = await self.client.get(url, params=params, headers=merged_headers)
        return response

    async def post(self, endpoint: str, json: Optional[Dict[str, Any]] = None,
                   headers: Optional[Dict[str, str]] = None) -> httpx.Response:
        url = f"{self.base_url}/{endpoint}"
        merged_headers = {**self.default_headers, **(headers or {})}
        response = await self.client.post(url, json=json, headers=merged_headers)
        return response

    async def close(self):
        await self.client.aclose()
