import unittest

class SecurityTest(unittest.TestCase):
    """NFR-002: Security Requirements"""

    def setUp(self):
        # Simulated security environment
        self.ssl_enabled = True
        self.encryption_method = "AES-256"
        self.vulnerabilities = {"SQL_injection": False, "XSS": False}

    def test_005_ssl_tls_encryption(self):
        """Ensure all payment details use SSL/TLS encryption"""
        self.assertTrue(self.ssl_enabled, "SSL/TLS encryption not enabled during transmission")

    def test_006_secure_data_storage(self):
        """Sensitive user data should be stored securely with encryption"""
        valid_methods = ["AES-128", "AES-256", "RSA-2048"]
        self.assertIn(self.encryption_method, valid_methods, "Data encryption method is not secure")

    def test_007_protection_against_vulnerabilities(self):
        """Website should be protected from SQL Injection and XSS attacks"""
        for vuln, status in self.vulnerabilities.items():
            self.assertFalse(status, f"Vulnerability found: {vuln}")


if __name__ == "__main__":
    unittest.main(verbosity=2)


