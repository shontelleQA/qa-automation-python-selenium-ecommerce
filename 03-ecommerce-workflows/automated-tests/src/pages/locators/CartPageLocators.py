# CartPageLocators.py
# -------------------
# Contains locator definitions for fields and buttons on the Cart page.

from selenium.webdriver.common.by import By


class CartPageLocators:
    # Text field where coupon codes are entered
    COUPON_FIELD = (By.ID, "coupon_code")

    # "Apply coupon" button
    APPLY_COUPON_BUTTON = (By.CSS_SELECTOR, "button[name='apply_coupon']")

    # Message banner shown after applying a coupon
    CART_PAGE_MESSAGE = (By.CLASS_NAME, "woocommerce-message")
