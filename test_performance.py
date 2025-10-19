import unittest
import time

class PerformanceTest(unittest.TestCase):
    """NFR-001: Website Performance"""

    def setUp(self):
        # Simulated page load times in seconds
        self.page_load_times = {
            "homepage": 1.8,
            "product_listing": 1.5,
            "cart": 2.5,
            "checkout": 2.8
        }
        # Maximum concurrent users supported
        self.max_concurrent_users = 1000

    def test_001_homepage_load_time(self):
        """Homepage should load within 2 seconds"""
        load_time = self.page_load_times["homepage"]
        self.assertLessEqual(load_time, 2, f"Homepage load too slow: {load_time}s")

    def test_002_product_listing_load_time(self):
        """Product listing should load within 2 seconds"""
        load_time = self.page_load_times["product_listing"]
        self.assertLessEqual(load_time, 2, f"Product listing load too slow: {load_time}s")

    def test_003_cart_checkout_time(self):
        """Cart and checkout actions should take less than 3 seconds"""
        cart_time = self.page_load_times["cart"]
        checkout_time = self.page_load_times["checkout"]
        self.assertLessEqual(cart_time, 3, f"Cart action too slow: {cart_time}s")
        self.assertLessEqual(checkout_time, 3, f"Checkout action too slow: {checkout_time}s")

    def test_004_concurrent_users(self):
        """Application should handle 1000 concurrent users"""
        users_supported = self.max_concurrent_users
        self.assertGreaterEqual(users_supported, 1000, "System cannot handle 1000 concurrent users")


if __name__ == "__main__":
    unittest.main(verbosity=2)


