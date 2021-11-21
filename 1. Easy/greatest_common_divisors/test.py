import unittest

from greatest_common_divisors import greatest_common_divisors

class TestCases(unittest.TestCase):
    def test_greatest_common_divisors(self):
        self.assertEqual(greatest_common_divisors([6, 12, 9]), 3)
        self.assertEqual(greatest_common_divisors([5, 10, 15, 20]), 5)
        self.assertEqual(greatest_common_divisors([1, 2, 3, 4, 5]), 1)
        self.assertEqual(greatest_common_divisors([4, 8, 12, 20]), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)