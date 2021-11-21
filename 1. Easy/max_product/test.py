import unittest

from max_product import max_product

class TestCases(unittest.TestCase):
    def test_max_product(self):
        self.assertEqual(max_product([5, 1, 7]), 35)
        self.assertEqual(max_product([-5, 1, -7]), 35)
        self.assertEqual(max_product([7, 1, 7]), 49)

if __name__ == "__main__":
    unittest.main(verbosity=2)