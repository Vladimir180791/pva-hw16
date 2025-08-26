from .base_page import BasePage
from locators.admin_locators import AdminLoginLocators

class AdminLoginPage(BasePage):
    def login(self, username, password):
        self.input_text(AdminLoginLocators.USERNAME_INPUT, username)
        self.input_text(AdminLoginLocators.PASSWORD_INPUT, password)
        self.click(AdminLoginLocators.LOGIN_BUTTON)

    def is_login_successful(self):
        return not self.is_element_present(AdminLoginLocators.ALERT_DANGER)