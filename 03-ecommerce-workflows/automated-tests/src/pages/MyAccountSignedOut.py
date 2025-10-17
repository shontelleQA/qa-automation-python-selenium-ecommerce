# src/pages/MyAccountSignedOut.py

class MyAccountSignedOut:
    """
    This class represents the My Account page when a user is signed out.
    It holds all the actions you can do on that page (like login or register).
    """

    def __init__(self, driver):
        # driver = the browser (from your fixture)
        self.driver = driver

    # Go to the My Account page
    def go_to_my_account(self):
        pass  # we'll add self.driver.get("...") later

    # Type username into the login box
    def input_login_username(self, username):
        pass  # will fill this in once locators are ready

    # Type password into the password box
    def input_login_password(self, password):
        pass

    # Click the login button
    def click_login_button(self):
        pass
