from e2e_tests.pages.base_page import BasePage


class ChatPage(BasePage):
    _email_input = '[data-test-id="login-email"]'

    async def chat(self):
        pass
