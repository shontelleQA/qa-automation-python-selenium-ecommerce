from src.helpers.selenium_extended import SeleniumExtended
from src.pages.locators.CartPageLocators import CartPageLocators
from src.configs.generic_configs import GenericConfigs
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time

class CartPage(CartPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    # --- Coupon actions ---

    def input_coupon(self, coupon_code):
        """Type the provided coupon code into the coupon field."""
        self.sl.wait_and_input_text(self.COUPON_FIELD, coupon_code)

    def click_apply_coupon(self):
        """Click the 'Apply coupon' button."""
        self.sl.wait_and_click(self.APPLY_COUPON_BUTTON)

    def get_displayed_message(self):
        """Return the success or error message shown after applying a coupon."""
        text = self.sl.wait_and_get_text(self.CART_PAGE_MESSAGE)
        return text

    def apply_coupon(self):
        """Clicks 'Add a coupon', applies code, verifies success banner."""
        toggle = self.driver.find_elements(*self.COUPON_TOGGLE)
        if toggle:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", toggle[0])
            self.sl.wait_and_click(self.COUPON_TOGGLE)

        # Wait for coupon input to appear
        self.sl.wait_until_element_is_visible(self.COUPON_FIELD, timeout=15)

        coupon_code = GenericConfigs.FREE_COUPON
        self.input_coupon(coupon_code)
        self.click_apply_coupon()

        # Wait for banner and assert success
        self.sl.wait_until_element_is_visible(self.CART_PAGE_MESSAGE, timeout=15)
        success_message = self.driver.find_element(*self.CART_PAGE_MESSAGE).text

        assert "coupon code" in success_message.lower() and "applied" in success_message.lower(), (
            f"Expected coupon applied message, got '{success_message}'"
        )

    def click_proceed_to_checkout(self):
        """Click 'Proceed to Checkout' on block-based WooCommerce carts."""
        retries = 2
        for attempt in range(retries):
            try:
                self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN, timeout=15)
                return
            except (StaleElementReferenceException, TimeoutException):
                time.sleep(2)
                if attempt == retries - 1:
                    raise
