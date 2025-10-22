# CartPage.py
# ------------
# Page object for the Cart page: handles coupons, shipping, and checkout navigation.

from src.helpers.selenium_extended import SeleniumExtended
from src.pages.locators.CartPageLocators import CartPageLocators
from src.configs.generic_configs import GenericConfigs   # we'll create this next


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
        """
        Full coupon workflow:
        1. Enter coupon
        2. Click apply
        3. Verify success message
        """
        coupon_code = GenericConfigs.FREE_COUPON
        self.input_coupon(coupon_code)
        self.click_apply_coupon()

        # Verify expected success message appears
        success_message = self.get_displayed_message()
        expected = "Coupon code applied successfully."
        assert success_message == expected, (
            f"Unexpected message after applying coupon. "
            f"Expected: '{expected}', Got: '{success_message}'"
        )
