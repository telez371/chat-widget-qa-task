import allure

from e2e_tests.pages.base_page import BasePage


class SendMessagePage(BasePage):
    _input_message = '[id="chat21-main-message-context"]'
    _send_button = '[id="chat21-button-send"]'
    _assertion_text = '[class="messages msg_sent"]'

    async def send_msg(self):
        test_message = "test"
        await self.fill(self._input_message, test_message)
        await self.click(self._send_button)

        with allure.step("Check if the message is in chat history"):
            all_texts = await self.inner_text(self._assertion_text)

            return test_message, all_texts
