import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
@pytest.mark.tcid13
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        """
        TCID-13: Verify a new user can register successfully.
        """

        # 1️⃣ Create the page object
        my_account = MyAccountSignedOut(self.driver)

        # 2️⃣ Go to My Account page
        my_account.go_to_my_account()

        # 3️⃣ Fill in registration form
        my_account.input_register_email("test1@example.com")  # temporary static email
        my_account.input_register_password("Password123!")

        # 4️⃣ Click the register button
        my_account.click_register_button()

        # 🧩 Expected Result:
        # After successful registration, the user should be logged in automatically
        # (we'll verify this in Lesson 134 when we add assertions)