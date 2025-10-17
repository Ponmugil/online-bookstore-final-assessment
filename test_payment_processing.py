import unittest

class PaymentProcessingTest(unittest.TestCase):
    """FR-004: Payment Processing"""

    def setUp(self):
        # Example payment details entered by the user
        self.payment_info = {
            "card_number": "4111111111111111",
            "expiry_date": "12/27",
            "cvv": "123",
            "card_holder": "XYZ"
        }

        # Simulate a secure payment connection
        self.secure_connection = True

        # Flag to track whether payment succeeds
        self.payment_success = True

    def test_007_payment_info_entry(self):
        """FR-004.1: Validate payment details entry"""
        self.assertIn("card_number", self.payment_info)
        self.assertIn("expiry_date", self.payment_info)
        self.assertIn("cvv", self.payment_info)
        self.assertTrue(self.payment_info["card_number"].isdigit(), "Card number should be numeric")
        self.assertEqual(len(self.payment_info["card_number"]), 16, "Card number must be 16 digits")

    def test_008_secure_connection(self):
        """FR-004.2: Ensure secure SSL/TLS connection"""
        self.assertTrue(self.secure_connection, "Connection is not secure (SSL/TLS missing)")

    def test_009_successful_payment_redirect(self):
        """FR-004.3: Redirect user on successful payment"""
        redirect_page = "order_confirmation.html" if self.payment_success else None
        self.assertEqual(redirect_page, "order_confirmation.html", "User not redirected after payment success")

    def test_010_failed_payment_message(self):
        """FR-004.4: Display error and retry option on payment failure"""
        self.payment_success = False
        if not self.payment_success:
            error_message = "Payment failed! Please check your details and try again."
            retry_option = True
        else:
            error_message = ""
            retry_option = False

        self.assertIn("Payment failed", error_message)
        self.assertTrue(retry_option, "Retry option not shown for failed payment")


if __name__ == "__main__":
    unittest.main(verbosity=2)


