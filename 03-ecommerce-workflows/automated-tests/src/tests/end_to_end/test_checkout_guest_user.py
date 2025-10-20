import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut  # we’ll reuse URL helper soon

@pytest.mark.usefixtures("init_driver")
class TestE2ECheckoutGuestUser:

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        """
        Steps we will implement across the next lessons:
        1) Go to Home page
        2) Add 2 items to cart (any simple products)
        3) Go to Cart
        4) Apply free coupon (QA100)
        5) Select Free Shipping
        6) Proceed to Checkout
        7) Fill Billing form (guest user)
        8) Place Order
        9) Verify 'Order received' page (and later capture Order #)
        """
        # We’ll fill these with real page objects in the next lessons
        assert True, "Scaffold ready — we’ll implement each step next."
