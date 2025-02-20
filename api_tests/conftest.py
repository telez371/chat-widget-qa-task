import pytest

from api_tests.core.api_client import ApiClient

pytest_plugins = [
    "api_tests.fixtures.chat_fixtures",
]


@pytest.fixture(scope="session")
async def api_client():
    async with ApiClient() as client:
        yield client
