import allure

from e2e_tests.pages.send_file_page import SendFilePage


class TestSendFile:
    @allure.feature("Chat Widget")
    @allure.story("Send File")
    @allure.title("Test sending a file in the chat widget")
    async def test_send_file(self, open_chat):
        with allure.step("Opening chat and initializing the SendFilePage"):
            chat_page = SendFilePage(open_chat, "https://autofaq.ai/")

        with allure.step("Uploading and sending a file"):
            await chat_page.send_file()

        with allure.step("Verifying if the file was successfully uploaded"):
            assert await chat_page.is_uploaded(), "The file didn't show up in the chat!"
