from .base_page import BasePage
from locators.admin_locators import AdminAddProductLocators

class AdminAddProductPage(BasePage):
    def fill_product_info(self, product_name, meta_tag, model, price, quantity):
        self.input_text(AdminAddProductLocators.PRODUCT_NAME, product_name)
        self.input_text(AdminAddProductLocators.META_TAG, meta_tag)
        
        self.click(AdminAddProductLocators.DATA_TAB)
        self.input_text(AdminAddProductLocators.MODEL, model)
        self.input_text(AdminAddProductLocators.PRICE, price)
        self.input_text(AdminAddProductLocators.QUANTITY, quantity)

    def save_product(self):
        self.click(AdminAddProductLocators.SAVE_BUTTON)