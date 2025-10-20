from src.helpers.config_helpers import get_base_url
from src.selenium_extended import SeleniumExtended

class HomePage:
    ENDPOINT = "/"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_home_page(self):
        self.driver.get(get_base_url() + self.ENDPOINT)

    # to be added in Part 2:
    # - click_first_product()
    # - add_first_product_to_cart()
    # - maybe a generic "add_product_to_cart_by_name(name)"
