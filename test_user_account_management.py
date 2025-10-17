import unittest

class UserAccountManagementTest(unittest.TestCase):
    """FR-006: User Account Management"""

    def setUp(self):
        self.users = {}
        self.logged_in_user = None
        self.orders = {
            "xyz@example.com": [
                {"book": "Python Basics", "price": "£300"},
                {"book": "Django Mastery", "price": "£500"}
            ]
        }

    def create_account(self, email, password):
        if email not in self.users:
            self.users[email] = {"password": password, "name": "", "address": ""}
            return True
        return False

    def login(self, email, password):
        if email in self.users and self.users[email]["password"] == password:
            self.logged_in_user = email
            return True
        return False

    def view_past_orders(self, email):
        return self.orders.get(email, [])

    def update_info(self, email, name=None, password=None):
        if email in self.users:
            if name:
                self.users[email]["name"] = name
            if password:
                self.users[email]["password"] = password
            return True
        return False

    def logout(self):
        self.logged_in_user = None
        return True

    def test_013_create_account(self):
        """Users should be able to create an account"""
        result = self.create_account("xyz@example.com", "secure123")
        self.assertTrue(result)
        self.assertIn("xyz@example.com", self.users)

    def test_014_login_and_view_orders(self):
        """After login, users should view their past orders"""
        self.create_account("xyz@example.com", "secure123")
        self.assertTrue(self.login("xyz@example.com", "secure123"))
        orders = self.view_past_orders("xyz@example.com")
        self.assertGreater(len(orders), 0)

    def test_015_update_personal_info(self):
        """Users should be able to update their personal info"""
        self.create_account("xyz@example.com", "secure123")
        updated = self.update_info("xyz@example.com", name="xyz", password="newpass123")
        self.assertTrue(updated)
        self.assertEqual(self.users["xyz@example.com"]["name"], "xyz")
        self.assertEqual(self.users["xyz@example.com"]["password"], "newpass123")

    def test_016_logout(self):
        """Users should be able to log out"""
        self.create_account("xyz@example.com", "secure123")
        self.login("xyz@example.com", "secure123")
        self.assertIsNotNone(self.logged_in_user)
        result = self.logout()
        self.assertTrue(result)
        self.assertIsNone(self.logged_in_user)

if __name__ == "__main__":
    unittest.main(verbosity=2)


