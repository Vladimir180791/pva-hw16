from .base_page import BasePage
from locators.admin_locators import AdminProductsLocators

class AdminProductsPage(BasePage):
    def click_add_new(self):
        self.click(AdminProductsLocators.ADD_NEW_BUTTON)

    def delete_product(self, product_name):
        # Find and select the product checkbox
        checkboxes = self.driver.find_elements(*AdminProductsLocators.PRODUCT_CHECKBOX)
        product_names = self.driver.find_elements(*AdminProductsLocators.PRODUCT_NAME_IN_LIST)
        
        for i, name_element in enumerate(product_names):
            if product_name in name_element.text:
                checkboxes[i].click()
                break
        
        self.click(AdminProductsLocators.DELETE_BUTTON)
        # Confirm alert
        self.driver.switch_to.alert.accept()

    def is_success_message_displayed(self):
        return self.is_element_present(AdminProductsLocators.SUCCESS_ALERT)