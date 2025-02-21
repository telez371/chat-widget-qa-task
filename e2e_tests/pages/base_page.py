import allure
from playwright.async_api import Page, expect


class BasePage:
    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url
        self.timeout = 40000

    async def open(self) -> None:
        with allure.step(f"Navigate to URL: {self.url}"):
            await self.page.goto(self.url)

    async def get_element(self, selector: str):
        element = self.page.locator(selector)
        await expect(element).to_be_attached(timeout=self.timeout)
        return element

    async def click(self, selector: str) -> None:
        with allure.step(f"Click on element: {selector}"):
            element = await self.get_element(selector)
            await expect(element).to_be_visible(timeout=self.timeout)
            await expect(element).to_be_enabled(timeout=self.timeout)
            await element.click()

    async def fill(self, selector: str, value: str) -> None:
        with allure.step(f"Fill element: {selector} with value: {value}"):
            element = await self.get_element(selector)
            await expect(element).to_be_visible(timeout=self.timeout)
            await expect(element).to_be_enabled(timeout=self.timeout)
            await expect(element).to_be_editable(timeout=self.timeout)
            await element.fill(value)

    async def inner_text(self, selector: str) -> str:
        with allure.step(f"Get inner text of element: {selector}"):
            element = await self.get_element(selector)
            await expect(element).to_be_visible(timeout=self.timeout)
            return await element.inner_text()

    async def upload_file(self, selector: str, file_path: str) -> None:
        with allure.step(f"Upload file: {file_path} to {selector}"):
            file_input = await self.get_element(selector)
            await file_input.set_input_files(file_path)

    async def is_file_uploaded(self, selector: str) -> bool:
        with allure.step(f"Check if file is uploaded to {selector}"):
            file_element = await self.get_element(selector)
            return await file_element.is_visible(timeout=self.timeout)
