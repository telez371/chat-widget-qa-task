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