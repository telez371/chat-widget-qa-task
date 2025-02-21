import allure
from e2e_tests.pages.base_page import BasePage


class SendSmilePage(BasePage):
    _smile_button = '[id="chat21-button-emoji"]'
    _smile_choosing = '[data-full-name="grinning,grinning face"]'
    _send_button = '[id="chat21-button-send"]'
    _assertion_text = '[class="messages msg_sent"]'

    @allure.step("Sending a smile emoji in the chat")
    async def send_smile(self):
        with allure.step("Clicking the emoji button"):
            await self.click(self._smile_button)

        with allure.step("Choosing a smile emoji"):
            await self.click(self._smile_choosing)

        with allure.step("Sending the emoji"):
            await self.click(self._send_button)

        with allure.step("Fetching sent message text for validation"):
            assertion_text = await self.inner_text(self._assertion_text)

        return assertion_text