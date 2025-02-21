from e2e_tests.pages.base_page import BasePage


class SendFilePage(BasePage):
    _file_upload_input = '[id="chat21-file"]'
    _send_button = '[id="chat21-button-send"]'
    _assertion_text = '[class="messages msg_sent"]'
    _file_attachment = '[class="display_attachment"]'

    async def send_file(self):
        file_path = "e2e_tests/images/XPath.jpeg"
        await self.upload_file(self._file_upload_input, file_path)
        await self.click(self._send_button)

    async def is_uploaded(self):
        return await self.is_file_uploaded(self._file_attachment)