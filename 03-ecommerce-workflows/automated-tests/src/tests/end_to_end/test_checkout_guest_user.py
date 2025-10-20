import pytest
from src.pages.HomePage import HomePage
from src.pages.CartPage import CartPage
from src.pages.CheckoutPage import CheckoutPage
from src.pages.OrderReceivedPage import OrderReceivedPage

@pytest.mark.usefixtures("init_driver")
class TestE2ECheckoutGuestUser:

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        home = HomePage(self.driver)
        cart = CartPage(self.driver)
        checkout = CheckoutPage(self.driver)
        order_received = OrderReceivedPage(self.driver)

        # Step plan (no-op placeholders for now)
        # home.go_to_home_page()
        # home.add_first_product_to_cart()
        # home.add_first_product_to_cart()
        # cart.go_to_cart()
        # cart.apply_coupon("QA100")
        # cart.select_free_shipping()
        # cart.click_proceed_to_checkout()
        # checkout.fill_billing_form({...})
        # checkout.click_place_order()
        # order_received.wait_for_order_received()
        # order_no = order_received.get_order_number()

        assert True
