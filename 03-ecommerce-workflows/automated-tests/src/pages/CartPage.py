from src.selenium_extended import SeleniumExtended

class CartPage:
    ENDPOINT = "/cart/"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    # to be added in Part 3:
    # - go_to_cart()
    # - apply_coupon("QA100")
    # - wait_for_coupon_applied()
    # - select_free_shipping()
    # - click_proceed_to_checkout()
