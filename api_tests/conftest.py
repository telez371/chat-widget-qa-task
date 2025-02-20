import pytest

from api_tests.core.api_client import ApiClient


@pytest.fixture
async def api_client():
    async with ApiClient() as client:
        yield client
