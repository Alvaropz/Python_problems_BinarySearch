import unittest

from largest_product_of_contiguous_digits import largest_product_of_contiguous_digits

class TestCases(unittest.TestCase):
    def test_largest_product_of_contiguous_digits(self):
        self.assertEqual(largest_product_of_contiguous_digits(41598671, 3), 432)
        self.assertEqual(largest_product_of_contiguous_digits(41598671, 1), 9)
        self.assertEqual(largest_product_of_contiguous_digits(41598671, 6), 15120)
        self.assertEqual(largest_product_of_contiguous_digits(41598671, 8), 60480)
        self.assertEqual(largest_product_of_contiguous_digits(77510373, 6), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)