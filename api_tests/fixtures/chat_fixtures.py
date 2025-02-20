import json
from http import HTTPStatus

import allure
import pytest

from api_tests.core.api_client import ApiClient
from api_tests.endpoints import Endpoints
from api_tests.models.users import UserPayload


@allure.feature("Authentication")
@allure.story("User Session Management")
@pytest.fixture(scope="session")
async def session_id(api_client: ApiClient) -> str:
    fake_user = UserPayload.generate_fake().model_dump(mode="json")
    allure.attach(json.dumps(fake_user, indent=2), "Generated User Data", allure.attachment_type.JSON)

    response = await api_client.post(Endpoints.USERS, json=fake_user)
    assert response.status_code == HTTPStatus.OK, f"Failed to create user. Expected 200, got {response.status_code}"

    session_id_str = response.json()["id"]
    allure.attach(session_id_str, "Generated Session ID", allure.attachment_type.TEXT)

    return session_id_str
