import unittest

from penny_for_your_thoughts import penny_for_your_thoughts

class TestCases(unittest.TestCase):
    def test_penny_for_your_thoughts(self):
        self.assertEqual(penny_for_your_thoughts(1), "0.01")
        self.assertEqual(penny_for_your_thoughts(12), "0.12")
        self.assertEqual(penny_for_your_thoughts(123), "1.23")
        self.assertEqual(penny_for_your_thoughts(1234), "12.34")
        self.assertEqual(penny_for_your_thoughts(12345), "123.45")
        self.assertEqual(penny_for_your_thoughts(123456), "1,234.56")
        self.assertEqual(penny_for_your_thoughts(1234567), "12,345.67")
        self.assertEqual(penny_for_your_thoughts(100000000), "1,000,000.00")

if __name__ == "__main__":
    unittest.main(verbosity=2)