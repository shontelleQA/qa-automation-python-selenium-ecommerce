import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
@pytest.mark.tcid13
class TestRegisterNewUser:

    def test_register_valid_new_user(self):
        my_account = MyAccountSignedOut(self.driver)

        # 1️⃣ Go to My Account page
        my_account.go_to_my_account()

        # 2️⃣ Fill in email + password
        my_account.input_register_email("test1@school.com")
        my_account.input_register_password("1234abc")

        # 3️⃣ Click Register
        my_account.click_register_button()

        # 4️⃣ (Verification will come later)
