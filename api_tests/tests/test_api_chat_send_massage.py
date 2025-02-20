import json
from http import HTTPStatus

import allure
import pytest

from api_tests.core.api_client import ApiClient
from api_tests.endpoints import Endpoints
from api_tests.models.messages import SendMessageRequest, SendMessageResponse

BOUNDARY = "----WebKitFormBoundaryquAj3e5ejXhibXAb"


class TestSendMessage:

    def _prepare_multipart_data(self, payload: dict, ) -> tuple[dict, str]:
        with allure.step("Prepare multipart data"):
            headers = {
                "Content-Type": f"multipart/form-data; boundary={BOUNDARY}",
                "session-id": self.session_id
            }

            data = (
                f"--{BOUNDARY}\r\n"
                f"Content-Disposition: form-data; name=\"payload\"\r\n\r\n"
                f"{json.dumps(payload)}\r\n"
                f"--{BOUNDARY}--\r\n"
            )
            allure.attach(json.dumps(payload, indent=2), name="Payload", attachment_type=allure.attachment_type.JSON)
            return headers, data

    @pytest.mark.asyncio(loop_scope="session")
    async def test_send_basic_message(self, api_client: ApiClient, session_id: str) -> None:
        with allure.step("Set session_id"):
            self.session_id = session_id

        with allure.step("Create request payload"):
            send_message = SendMessageRequest(text="test message from api").model_dump(mode="json")
            headers, data = self._prepare_multipart_data(send_message)

        with allure.step("Send request"):
            response = await api_client.post(Endpoints.MESSAGES, headers=headers, content=data)
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Validate response"):
            assert response.status_code == HTTPStatus.OK, f"Expected 200 OK, got {response.status_code}"
            response_data = SendMessageResponse.model_validate(response.json())
            assert response_data.text == send_message["text"]

    @pytest.mark.asyncio(loop_scope="session")
    async def test_send_empty_message(self, api_client: ApiClient, session_id: str) -> None:
        with allure.step("Set session_id"):
            self.session_id = session_id

        with allure.step("Create request with empty message"):
            send_message = SendMessageRequest(text="").model_dump(mode="json")
            headers, data = self._prepare_multipart_data(send_message)

        with allure.step("Send request"):
            response = await api_client.post(Endpoints.MESSAGES, headers=headers, content=data)
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Validate response"):
            assert response.status_code == HTTPStatus.OK, f"Expected 200 OK, got {response.status_code}"
            response_data = SendMessageResponse.model_validate(response.json())
            assert response_data.text == ""

    @pytest.mark.asyncio(loop_scope="session")
    async def test_send_long_message(self, api_client: ApiClient, session_id: str) -> None:
        with allure.step("Set session_id"):
            self.session_id = session_id

        with allure.step("Create request with long message"):
            long_text = "A" * 4000
            send_message = SendMessageRequest(text=long_text).model_dump(mode="json")
            headers, data = self._prepare_multipart_data(send_message)

        with allure.step("Send request"):
            response = await api_client.post(Endpoints.MESSAGES, headers=headers, content=data)
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Validate response"):
            assert response.status_code == HTTPStatus.OK, f"Expected 200 OK, got {response.status_code}"
            response_data = SendMessageResponse.model_validate(response.json())
            assert response_data.text == long_text

    @pytest.mark.asyncio(loop_scope="session")
    async def test_send_special_characters(self, api_client: ApiClient, session_id: str) -> None:
        with allure.step("Set session_id"):
            self.session_id = session_id

        with allure.step("Create request with special characters"):
            special_text = "!@#$%^&*()_+{}[]|\\:;\"'<>,.?/~`测试"
            send_message = SendMessageRequest(text=special_text).model_dump(mode="json")
            headers, data = self._prepare_multipart_data(send_message)

        with allure.step("Send request"):
            response = await api_client.post(Endpoints.MESSAGES, headers=headers, content=data)
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Validate response"):
            assert response.status_code == HTTPStatus.OK, f"Expected 200 OK, got {response.status_code}"
            response_data = SendMessageResponse.model_validate(response.json())
            assert response_data.text == special_text

    @pytest.mark.asyncio(loop_scope="session")
    async def test_send_without_session_id(self, api_client: ApiClient) -> None:
        with allure.step("Create request without session_id"):
            send_message = SendMessageRequest(text="test message").model_dump(mode="json")

            headers = {"Content-Type": f"multipart/form-data; boundary={BOUNDARY}"}
            data = (f"--{BOUNDARY}\r\nContent-Disposition: form-data;"
                    f" name=\"payload\"\r\n\r\n{json.dumps(send_message)}\r\n--{BOUNDARY}--\r\n")

        with allure.step("Send request"):
            response = await api_client.post(Endpoints.MESSAGES, headers=headers, content=data)
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Validate response"):
            assert response.status_code == HTTPStatus.OK, f"Expected 200 OK, got {response.status_code}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_send_invalid_json(self, api_client: ApiClient, session_id: str) -> None:
        with allure.step("Set session_id"):
            self.session_id = session_id

        with allure.step("Create request with invalid JSON"):
            headers = {
                "Content-Type": f"multipart/form-data; boundary={BOUNDARY}",
                "session-id": session_id
            }
            data = f"--{BOUNDARY}\r\nContent-Disposition: form-data; name=\"payload\"\r\n\r\ninvalid json{{\r\n--{BOUNDARY}--\r\n"

        with allure.step("Send request"):
            response = await api_client.post(Endpoints.MESSAGES, headers=headers, content=data)
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Validate response"):
            assert response.status_code == HTTPStatus.BAD_REQUEST, f"Expected 400, got {response.status_code}"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_send_multiple_messages(self, api_client: ApiClient, session_id: str) -> None:
        with allure.step("Set session_id"):
            self.session_id = session_id

        messages = ["Message 1", "Message 2", "Message 3"]
        for text in messages:
            with allure.step(f"Send message: {text}"):
                send_message = SendMessageRequest(text=text).model_dump(mode="json")
                headers, data = self._prepare_multipart_data(send_message)

                response = await api_client.post(Endpoints.MESSAGES, headers=headers, content=data)
                allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

                assert response.status_code == HTTPStatus.OK, f"Expected 200 OK, got {response.status_code}"
                response_data = SendMessageResponse.model_validate(response.json())
                assert response_data.text == text
