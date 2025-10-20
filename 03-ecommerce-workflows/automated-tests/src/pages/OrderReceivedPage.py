from src.selenium_extended import SeleniumExtended

class OrderReceivedPage:
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    # to be added in Part 5:
    # - wait_for_order_received()
    # - get_order_number()
