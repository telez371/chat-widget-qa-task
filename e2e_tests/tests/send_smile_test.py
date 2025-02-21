import allure
from e2e_tests.pages.send_smile_page import SendSmilePage


class TestSendSmile:
    @allure.feature("Chat Widget")
    @allure.story("Send Smile Emoji")
    @allure.title("Sending a smile emoji and verifying it appears in chat")
    async def test_send_smile(self, open_chat):
        chat_page = SendSmilePage(open_chat, "https://autofaq.ai/")

        with allure.step("Performing emoji send action"):
            assertion_text = await chat_page.send_smile()

        with allure.step("Validating that the sent emoji is correct"):
            assert assertion_text == "🤣", f"Expected '🤣', but got '{assertion_text}'"