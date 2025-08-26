from .base_page import BasePage
from locators.main_locators import RegisterPageLocators

class RegisterPage(BasePage):
    def register_user(self, first_name, last_name, email, telephone, password):
        self.input_text(RegisterPageLocators.FIRST_NAME, first_name)
        self.input_text(RegisterPageLocators.LAST_NAME, last_name)
        self.input_text(RegisterPageLocators.EMAIL, email)
        self.input_text(RegisterPageLocators.TELEPHONE, telephone)
        self.input_text(RegisterPageLocators.PASSWORD, password)
        self.input_text(RegisterPageLocators.CONFIRM_PASSWORD, password)
        self.click(RegisterPageLocators.PRIVACY_POLICY)
        self.click(RegisterPageLocators.CONTINUE_BUTTON)

    def is_registration_successful(self):
        success_text = self.get_text(RegisterPageLocators.SUCCESS_MESSAGE)
        return "Your Account Has Been Created!" in success_text