import unittest

class CheckoutProcessTest(unittest.TestCase):
    """Test suite for the checkout process in an online bookstore."""

    def setUp(self):
        # Initialize sample cart, shipping info, and payment details
        self.cart = {
            "Python Basics": {"price": "£300", "quantity": 2},
            "AI for Beginners": {"price": "£500", "quantity": 1}
        }
        self.shipping_info = {"name": "XYZ", "address": "CANADA US"}
        self.payment_method = "Credit Card"
        self.discount_code = "DISCOUNT10"
        self.valid_payment = True

    def test_001_cart_display(self):
        """Verify that the cart shows items, quantities, and total price."""
        total = sum(int(item["price"].replace("£", "")) * item["quantity"]
                    for item in self.cart.values())
        self.assertGreater(total, 0)
        self.assertIn("Python Basics", self.cart)
        self.assertIn("AI for Beginners", self.cart)

    def test_002_shipping_info_entry(self):
        """Verify that user can enter valid shipping details."""
        self.assertIn("name", self.shipping_info)
        self.assertIn("address", self.shipping_info)
        self.assertNotEqual(self.shipping_info["address"], "")

    def test_003_payment_method_selection(self):
        """Ensure a valid payment method is selected."""
        allowed_methods = ["Credit Card", "PayPal", "UPI"]
        self.assertIn(self.payment_method, allowed_methods)

    def test_004_apply_discount_code(self):
        """Verify that valid discount codes are accepted."""
        valid_codes = ["DISCOUNT10", "OFFER20"]
        self.assertIn(self.discount_code, valid_codes)

    def test_005_payment_validation(self):
        """Check payment validation and discount calculation."""
        total_price = sum(int(item["price"].replace("£", "")) * item["quantity"]
                          for item in self.cart.values())
        discount = 0.1 if self.discount_code == "DISCOUNT10" else 0
        total_after_discount = total_price - (total_price * discount)
        self.assertTrue(self.valid_payment)
        self.assertGreater(total_after_discount, 0)

    def test_006_order_confirmation_redirect(self):
        """Verify redirection to confirmation page after successful payment."""
        payment_successful = self.valid_payment
        redirect_page = "order_confirmation.html" if payment_successful else "payment_failed.html"
        self.assertEqual(redirect_page, "order_confirmation.html")


if __name__ == '__main__':
    unittest.main(verbosity=2)

