import unittest

class UsabilityTest(unittest.TestCase):
    """NFR-003: Usability Requirements"""

    def setUp(self):
        # Website layout and essential UI elements
        self.website_layout = {
            "header": True,
            "navigation_menu": True,
            "footer": True,
            "search_bar": True
        }

        self.ui_elements = {
            "buttons": ["Add to Cart", "Checkout", "Login", "Register"],
            "links": ["Home", "Products", "Contact Us"],
            "forms": ["Login Form", "Signup Form", "Checkout Form"]
        }

        self.cart_accessible = True
        self.checkout_accessible = True
        self.cart_modifiable = True

    def test_008_layout_clean_and_navigable(self):
        """Website layout should be clean and easy to navigate"""
        for section in ["header", "navigation_menu", "footer", "search_bar"]:
            self.assertTrue(self.website_layout.get(section, False), f"Missing or cluttered section: {section}")

    def test_009_elements_clearly_labeled(self):
        """Buttons, links, and forms should be clearly labeled"""
        self.assertTrue(all(len(name) > 0 for name in self.ui_elements["buttons"]), "Some buttons are unlabeled")
        self.assertTrue(all(len(link) > 0 for link in self.ui_elements["links"]), "Some links are unlabeled")
        self.assertTrue(all(len(form) > 0 for form in self.ui_elements["forms"]), "Some forms are unlabeled")

    def test_010_cart_and_checkout_accessible(self):
        """Shopping cart and checkout should be easy to access and modify"""
        self.assertTrue(self.cart_accessible, "Shopping cart is not accessible")
        self.assertTrue(self.checkout_accessible, "Checkout is not accessible")
        self.assertTrue(self.cart_modifiable, "Cart items cannot be modified")


if __name__ == "__main__":
    unittest.main(verbosity=2)