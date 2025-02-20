from asyncio import sleep

import allure

from e2e_tests.pages.chat_page import ChatPage


class TestChat:
    @allure.title('Successful login with generated credentials')
    @allure.severity(allure.severity_level.CRITICAL)
    async def test_open_chat(self, page):
        login_page = ChatPage(page, "https://autofaq.ai/")

        with allure.step('Open chat page'):
            await login_page.open()
            await sleep(60)
        # with allure.step('Perform chat'):
        #     assertion_text = login_page.chat()
