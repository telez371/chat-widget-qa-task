import allure
import pytest
from playwright.async_api import Page

from e2e_tests.pages.open_chat_page import OpenChatPage


@pytest.fixture
@allure.feature("Chat Widget")
@allure.story("Open Chat")
@allure.title("Opening the chat widget and verifying the title")
async def open_chat(page: Page):
    with allure.step("Initializing OpenChatPage and navigating to the chat page"):
        chat_page = OpenChatPage(page, "https://autofaq.ai/")
        await chat_page.open()

    with allure.step("Opening the chat widget"):
        assertion_text = await chat_page.open_chat()

    with allure.step("Verifying the chat title"):
        assert assertion_text == "AutoFAQ.ai", f"Expected 'AutoFAQ.ai', but got '{assertion_text}'"

    yield page
