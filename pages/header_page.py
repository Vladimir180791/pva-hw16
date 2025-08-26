from .base_page import BasePage
from locators.main_locators import MainPageLocators

class HeaderPage(BasePage):
    def switch_currency(self, currency_name):
        self.click(MainPageLocators.CURRENCY_DROPDOWN)
        
        if currency_name.upper() == "EUR":
            self.click(MainPageLocators.EURO_OPTION)
        elif currency_name.upper() == "GBP":
            self.click(MainPageLocators.POUND_OPTION)
        else:
            self.click(MainPageLocators.DOLLAR_OPTION)

    def get_current_currency_symbol(self):
        price_element = self.wait.until(EC.visibility_of_element_located(MainPageLocators.PRICE_ELEMENT))
        price_text = price_element.text
        return price_text[0]  # Get the currency symbol