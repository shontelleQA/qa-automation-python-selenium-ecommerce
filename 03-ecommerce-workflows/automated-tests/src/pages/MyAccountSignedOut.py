from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators as L
from src.selenium_extended import SeleniumExtended   # 👈 new import
from src.helpers.config_helpers import get_base_url


class MyAccountSignedOut:
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)           # 👈 new line

    def go_to_my_account(self):
        base_url = get_base_url()
        endpoint = "/my-account/"
        full_url = base_url + endpoint
        self.driver.get(full_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(L.LOGIN_USERNAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(L.LOGIN_PASSWORD, password)

    def click_login_button(self):
        self.sl.wait_and_click(L.LOGIN_BUTTON)
