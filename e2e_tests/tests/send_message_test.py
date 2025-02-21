import allure

from e2e_tests.pages.send_message_page import SendMessagePage


class TestSendMessage:
    @allure.feature("Chat Widget")
    @allure.story("Send Message")
    @allure.title("Test sending a message in the chat widget")
    async def test_send_message(self, open_chat):
        with allure.step("Opening chat and initializing the SendMessagePage"):
            chat_page = SendMessagePage(open_chat, "https://autofaq.ai/")

        with allure.step("Sending a test message"):
            test_message, assertion_text = await chat_page.send_msg()

        with allure.step("Verifying if the message was sent successfully"):
            assert test_message == assertion_text, \
                f"Expected: '{test_message}', but got: '{assertion_text}'"
