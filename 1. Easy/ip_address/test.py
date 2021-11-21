import unittest

from ip_address import ip_address

class TestCases(unittest.TestCase):
    def test_ip_address(self):
        self.assertEqual(ip_address("0.0.0.0"), True)
        self.assertEqual(ip_address("0.1.2.256"), False)
        self.assertEqual(ip_address("0.1.2.256"), False)
        self.assertEqual(ip_address("a.b.c.d"), False)
        self.assertEqual(ip_address("1.1.1"), False)
        self.assertEqual(ip_address("255.255.255.255"), True)
        self.assertEqual(ip_address("00.255.255.255"), False)
        self.assertEqual(ip_address("0.065.255.255"), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)