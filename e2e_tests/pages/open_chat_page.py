import allure

from e2e_tests.pages.base_page import BasePage


class OpenChatPage(BasePage):
    _chat_button = '[id="chat21-launcher-button"]'
    _chat_text = '[class="chat21-sheet-header-title"]'

    @allure.step("Opening the chat widget")
    async def open_chat(self):
        with allure.step("Clicking the chat button"):
            await self.click(self._chat_button)

        with allure.step("Fetching the chat header text"):
            text_title = await self.inner_text(self._chat_text)

        return text_title
