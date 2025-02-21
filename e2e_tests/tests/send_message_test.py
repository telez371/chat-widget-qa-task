from asyncio import sleep

import allure

from e2e_tests.pages.send_message_page import SendMessagePage


class TestSendMessage:
    async def test_send_message(self, open_chat):
        open_chat = SendMessagePage(open_chat, "https://autofaq.ai/")

        with allure.step('Perform chat'):
            test_message, assertion_text = await open_chat.send_msg()

            assert test_message == assertion_text
