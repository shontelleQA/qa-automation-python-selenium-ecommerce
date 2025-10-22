# CheckoutPage.py
# ----------------
# Page object for the Checkout page: handles billing, placing orders, and validation.

from src.helpers.selenium_extended import SeleniumExtended
from src.pages.locators.CheckoutPageLocators import CheckoutPageLocators

class CheckoutPage:
    ENDPOINT = "/checkout/"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    # to be added in Part 4:
    # - fill_billing_first_name/last_name/etc (or one method fill_billing_form(data))
    # - click_place_order()
