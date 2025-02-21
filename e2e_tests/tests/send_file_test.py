import allure

from e2e_tests.pages.send_file_page import SendFilePage


class TestSendFile:
    async def test_send_file(self, open_chat):
        open_chat = SendFilePage(open_chat, "https://autofaq.ai/")

        with allure.step('Perform chat'):
            await open_chat.send_file()

        with allure.step('We check that the file has been uploaded successfully'):
            assert await open_chat.is_uploaded(), "The file didn't show up in the chat!"
