import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Remove for visible browser
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    yield driver
    driver.quit()

@pytest.fixture
def admin_login(driver):
    from pages.admin_login_page import AdminLoginPage
    from data.test_data import TestData
    
    driver.get(TestData.ADMIN_URL)
    login_page = AdminLoginPage(driver)
    login_page.login(TestData.ADMIN_USERNAME, TestData.ADMIN_PASSWORD)
    return driver