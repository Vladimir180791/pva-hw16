from .base_page import BasePage
from locators.main_locators import MainPageLocators

class MainPage(BasePage):
    def go_to_register_page(self):
        self.click(MainPageLocators.MY_ACCOUNT)
        self.click(MainPageLocators.REGISTER)