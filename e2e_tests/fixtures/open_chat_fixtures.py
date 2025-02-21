import allure
import pytest
from playwright.async_api import Page

from e2e_tests.pages.open_chat_page import OpenChatPage


@pytest.fixture
async def open_chat(page: Page):
    open_chat = OpenChatPage(page, "https://autofaq.ai/")
    await open_chat.open()

    with allure.step('Open chat'):
        assertion_text = await open_chat.open_chat()

        assert assertion_text == "AutoFAQ.ai"

        yield page
