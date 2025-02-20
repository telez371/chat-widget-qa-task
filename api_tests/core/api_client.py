import httpx

from api_tests.core.config import Config


class ApiClient:
    def __init__(self):
        self.base_url = Config().BASE_URL
        self._client = None

    async def __aenter__(self):
        self._client = httpx.AsyncClient(
            headers={
                "Accept": "application/json",
            },
            base_url=self.base_url
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._client:
            await self._client.aclose()

    async def get(self, endpoint: str, **kwargs) -> httpx.Response:
        return await self._client.get(endpoint, **kwargs)

    async def post(self, endpoint: str, **kwargs) -> httpx.Response:
        return await self._client.post(endpoint, **kwargs)
