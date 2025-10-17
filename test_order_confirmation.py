import unittest

class OrderConfirmationTest(unittest.TestCase):
    """Test suite for order confirmation and post-payment process."""

    def setUp(self):
        # Simulated payment status (True = successful payment)
        self.payment_success = True

        # Example order details
        self.order_details = {
            "items": [
                {"name": "Python Basics", "price": "£300", "quantity": 2},
                {"name": "AI for Beginners", "price": "£500", "quantity": 1}
            ],
            "shipping_address": "Canada, USA"
        }

        self.email_sent = False
        self.confirmation_page_loaded = False

    def send_confirmation_email(self, order):
        """Simulate sending an order confirmation email."""
        if self.payment_success:
            self.email_sent = True
            return {
                "to": "user@example.com",
                "subject": "Your Order Confirmation",
                "body": f"Order Details: {order}"
            }
        return None

    def load_confirmation_page(self, order):
        """Simulate loading the confirmation page after successful payment."""
        if self.payment_success:
            self.confirmation_page_loaded = True
            return {
                "page": "order_confirmation.html",
                "order_details": order
            }
        return None

    def test_011_order_confirmation_email_sent(self):
        """User should receive an order confirmation email after payment."""
        email = self.send_confirmation_email(self.order_details)
        self.assertTrue(self.email_sent, "Confirmation email not sent")
        self.assertIsNotNone(email, "Email content is empty")
        self.assertIn("Order Details", email["body"])
        self.assertIn("subject", email)
        self.assertIn("to", email)

    def test_012_order_summary_page_display(self):
        """Confirmation page should display correct order details."""
        confirmation_page = self.load_confirmation_page(self.order_details)

        self.assertTrue(self.confirmation_page_loaded, "Order confirmation page not loaded")
        self.assertIsNotNone(confirmation_page)
        self.assertEqual(confirmation_page["page"], "order_confirmation.html")
        self.assertIn("order_details", confirmation_page)
        self.assertIn("shipping_address", confirmation_page["order_details"])

        total = sum(
            int(str(item["price"]).replace("£", "")) * item["quantity"]
            for item in self.order_details["items"]
        )
        self.assertGreater(total, 0, "Total price should be positive")


if __name__ == '__main__':
    unittest.main(verbosity=2)















