import allure

from e2e_tests.pages.base_page import BasePage


class SendFilePage(BasePage):
    _file_upload_input = '[id="chat21-file"]'
    _send_button = '[id="chat21-button-send"]'
    _assertion_text = '[class="messages msg_sent"]'
    _file_attachment = '[class="display_attachment"]'

    @allure.step("Uploading a file to the chat widget")
    async def send_file(self):
        file_path = "e2e_tests/images/XPath.jpeg"

        with allure.step(f"Uploading file: {file_path}"):
            await self.upload_file(self._file_upload_input, file_path)

        with allure.step("Clicking the send button"):
            await self.click(self._send_button)

    @allure.step("Checking if the file was successfully uploaded")
    async def is_uploaded(self):
        return await self.is_file_uploaded(self._file_attachment)
