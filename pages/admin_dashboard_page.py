from .base_page import BasePage
from locators.admin_locators import AdminDashboardLocators

class AdminDashboardPage(BasePage):
    def navigate_to_products(self):
        self.click(AdminDashboardLocators.CATALOG_MENU)
        self.click(AdminDashboardLocators.PRODUCTS_MENU_ITEM)

    def logout(self):
        self.click(AdminDashboardLocators.LOGOUT_BUTTON)