import pytest

from api_tests.core.api_client import ApiClient
from api_tests.core.config import Config


@pytest.fixture(scope="session")
async def api_client() -> ApiClient:
    config = Config()
    client = ApiClient(config)
    yield client
    await client.close()
