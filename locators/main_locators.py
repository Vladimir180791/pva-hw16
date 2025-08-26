from selenium.webdriver.common.by import By

class MainPageLocators:
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, ".btn-link > .fa-caret-down")
    CURRENCY_OPTIONS = (By.CSS_SELECTOR, ".currency .dropdown-menu li")
    EURO_OPTION = (By.NAME, "EUR")
    POUND_OPTION = (By.NAME, "GBP")
    DOLLAR_OPTION = (By.NAME, "USD")
    PRICE_ELEMENT = (By.CSS_SELECTOR, ".price")
    MY_ACCOUNT = (By.CSS_SELECTOR, ".fa-user")
    REGISTER = (By.LINK_TEXT, "Register")

class RegisterPageLocators:
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM_PASSWORD = (By.ID, "input-confirm")
    PRIVACY_POLICY = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content h1")