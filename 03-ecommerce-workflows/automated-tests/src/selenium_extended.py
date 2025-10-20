# selenium_extended.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumExtended:
    """
    A helper class that gives us reusable Selenium actions
    so we don't have to repeat code in every test.
    """

    def __init__(self, driver, default_timeout=10):
        # This runs automatically when we create the class.
        # 'driver' is the browser, and default_timeout is how long to wait.
        self.driver = driver
        self.default_timeout = default_timeout

    def wait_and_input_text(self, locator, text, timeout=None):
        """
        Wait for an element to appear, then type text into it.
        Example:
            self.sl.wait_and_input_text(L.USERNAME_FIELD, "myname")
        """
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        """
        Wait for an element to appear, then click it.
        Example:
            self.sl.wait_and_click(L.LOGIN_BUTTON)
        """
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        """
        Wait until the given element contains the expected text.
        """
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )
