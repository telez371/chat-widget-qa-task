from asyncio import sleep

import allure

from e2e_tests.generator.generator import generated_person
from e2e_tests.pages.base_page import BasePage


class UserIdentificationPage(BasePage):
    _input_name = '[id="user-form_field_senderFullName"]'
    _input_email = '[id="user-form_field_senderEmail"]'
    _submit_button = '[class="form_panel_action form_panel_action-submit"]'
    _assertion_text = '[class="chat21-header-modal-select"]'

    @allure.step("Filling out the user identification form")
    async def user_identification(self):
        person = generated_person()

        with allure.step(f"Entering user name: {person.first_name}"):
            await self.fill(self._input_name, person.first_name)

        with allure.step(f"Entering user email: {person.email}"):
            await self.fill(self._input_email, person.email)

        with allure.step("Waiting before submitting the form (15 sec)"):
            await sleep(15)

        with allure.step("Submitting the form"):
            await self.click(self._submit_button)

        with allure.step("Verifying confirmation text"):
            assertion_text = await self.inner_text(self._assertion_text)

        return assertion_text
