from http import HTTPStatus

import pytest

from api_tests.core.api_client import ApiClient
from api_tests.endpoints import Endpoints


class TestRequests:
    @pytest.mark.asyncio
    async def test_post_anything(self, api_client: ApiClient) -> None:
        response = await api_client.post(
            Endpoints.USERS,
            json={
                "id": "63d7194d-fe5b-4b6b-8e9b-0635a8473294",
                "login": "63d7194d-fe5b-4b6b-8e9b-0635a8473294",
                "email": "test@test.ru",
                "fullName": "test",
                "payload": {}
            }
        )
        assert response.status_code == HTTPStatus.OK
