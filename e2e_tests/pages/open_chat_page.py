from e2e_tests.pages.base_page import BasePage


class OpenChatPage(BasePage):
    _chat_button = '[id="chat21-launcher-button"]'
    _chat_text = '[class="chat21-sheet-header-title"]'

    async def open_chat(self):
        await self.click(self._chat_button)
        text_title = await self.inner_text(self._chat_text)
        return text_title
