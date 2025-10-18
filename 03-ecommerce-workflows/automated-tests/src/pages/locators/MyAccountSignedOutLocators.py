# src/pages/locators/MyAccountSignedOutLocators.py
from selenium.webdriver.common.by import By

class MyAccountSignedOutLocators:
    # Login form elements
    LOGIN_USERNAME = (By.ID, "username")            # <input id="username">
    LOGIN_PASSWORD = (By.ID, "password")            # <input id="password">
    LOGIN_BUTTON  = (By.CSS_SELECTOR, "button[name='login']")  # <button name="login">

    # We'll add an error message locator later when we verify TCID-12
    # ERROR_MESSAGE = (By.CSS_SELECTOR, "ul.woocommerce-error li")  # (example if using WooCommerce)
