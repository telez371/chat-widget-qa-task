import os
import shutil
from datetime import datetime
from typing import AsyncGenerator

import aiofiles
import allure
import pytest
from playwright.async_api import async_playwright, Browser, BrowserContext, Page

pytest_plugins = [
    "e2e_tests.fixtures.open_chat_fixtures",
]


@pytest.fixture(scope="function")
async def browser() -> AsyncGenerator[Browser, None]:
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            chromium_sandbox=False,
            ignore_default_args=['--enable-automation']
        )
        yield browser
        await browser.close()


@pytest.fixture(scope="function")
async def context(browser: Browser) -> AsyncGenerator[BrowserContext, None]:
    context = await browser.new_context(record_video_dir="videos")

    context._has_failed_tests = False

    yield context

    if not context._has_failed_tests:
        try:
            shutil.rmtree("videos")
            os.makedirs("videos")
        except Exception as e:
            print(f"Ошибка при удалении видео: {e}")

    await context.close()


@pytest.fixture(scope="function")
async def page(context: BrowserContext) -> AsyncGenerator[Page, None]:
    page = await context.new_page()
    yield page

    if hasattr(page, "_failed") and page._failed:
        await attach_screenshot(page)
        await attach_video(page)
        context._has_failed_tests = True

    await page.close()


async def attach_screenshot(page: Page) -> None:
    try:
        screenshot_bytes = await page.screenshot(full_page=True)
        allure.attach(
            screenshot_bytes,
            name=f"Screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}",
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        print(f'Failed to attach screenshot: {e}')


async def attach_video(page: Page) -> None:
    try:
        video_path = await page.video.path()
        async with aiofiles.open(video_path, "rb") as video_file:
            video_bytes = await video_file.read()
            allure.attach(
                video_bytes,
                name=f"Video_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}",
                attachment_type=allure.attachment_type.MP4
            )
    except Exception as e:
        print(f'Failed to attach video: {e}')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if 'page' in item.fixturenames:
            page = item.funcargs['page']
            setattr(page, "_failed", True)
