import allure

from e2e_tests.pages.user_identification_page import UserIdentificationPage


class TestUserIdentification:
    @allure.feature("Chat Widget")
    @allure.story("User Identification")
    @allure.title("Test for entering name and email in the chat widget")
    async def test_user_identification(self, open_chat):
        with allure.step("Opening chat and initializing the identification page"):
            identification = UserIdentificationPage(open_chat, "https://autofaq.ai/")

        with allure.step("Starting the user identification process"):
            assertion_text = await identification.user_identification()

        with allure.step("Verifying confirmation text"):
            assert assertion_text == "Напишите свой вопрос и я постараюсь вам помочь", \
                f"Expected: 'Напишите свой вопрос и я постараюсь вам помочь', but got: '{assertion_text}'"
