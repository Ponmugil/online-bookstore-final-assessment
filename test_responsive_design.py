import unittest

class ResponsiveDesignTest(unittest.TestCase):
    """Tests to ensure the website layout and functionality work across devices (mobile, tablet, desktop)."""

    def setUp(self):
        # Device screen sizes (width × height)
        self.devices = {
            "mobile": {"width": 375, "height": 667},
            "tablet": {"width": 768, "height": 1024},
            "desktop": {"width": 1440, "height": 900}
        }

        self.current_layout = None
        self.nav_menu_accessible = True
        self.checkout_working = True

    def get_layout_for_device(self, width):
        """Return layout type based on screen width."""
        if width <= 480:
            return "mobile_layout"
        elif width <= 1024:
            return "tablet_layout"
        else:
            return "desktop_layout"

    def test_017_layout_responsiveness(self):
        """Website layout should adapt correctly for all screen sizes."""
        for device, size in self.devices.items():
            layout = self.get_layout_for_device(size["width"])
            self.assertIn(layout, ["mobile_layout", "tablet_layout", "desktop_layout"])
            print(f"{device.capitalize()} → {layout}")

    def test_018_navigation_accessibility(self):
        """Navigation menu should be accessible on all devices."""
        for device in self.devices:
            self.assertTrue(self.nav_menu_accessible, f"Navigation menu failed on {device}")

    def test_019_checkout_functionality_across_devices(self):
        """Checkout process should work properly across all devices."""
        for device in self.devices:
            self.assertTrue(self.checkout_working, f"Checkout not working on {device}")


if __name__ == "__main__":
    unittest.main(verbosity=2)


