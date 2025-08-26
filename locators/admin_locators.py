from selenium.webdriver.common.by import By

class AdminLoginLocators:
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    ALERT_DANGER = (By.CSS_SELECTOR, ".alert-danger")

class AdminDashboardLocators:
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCTS_MENU_ITEM = (By.LINK_TEXT, "Products")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".fa-sign-out")

class AdminProductsLocators:
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, ".fa-plus")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".fa-trash-o")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][name='selected[]']")
    PRODUCT_NAME_IN_LIST = (By.CSS_SELECTOR, "td.text-left")

class AdminAddProductLocators:
    PRODUCT_NAME = (By.ID, "input-name1")
    META_TAG = (By.ID, "input-meta-title1")
    MODEL = (By.ID, "input-model")
    PRICE = (By.ID, "input-price")
    QUANTITY = (By.ID, "input-quantity")
    DATA_TAB = (By.LINK_TEXT, "Data")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".fa-save")