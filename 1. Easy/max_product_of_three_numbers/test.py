import unittest

from max_product_of_three_numbers import max_product_of_three_numbers

class TestCases(unittest.TestCase):
    def test_max_product_of_three_numbers(self):
        self.assertEqual(max_product_of_three_numbers([5,4,1,3,-2,-2]), 60)
        self.assertEqual(max_product_of_three_numbers([5,4,1]), 20)
        self.assertEqual(max_product_of_three_numbers([-2,-2,-2]), -8)
        self.assertEqual(max_product_of_three_numbers([1,3,-2,0]), 0)
        self.assertEqual(max_product_of_three_numbers([0,2,-2,-2]), 8)
        self.assertEqual(max_product_of_three_numbers([-3,1,1,0]), 0)
        self.assertEqual(max_product_of_three_numbers([-3,-5,0,1]), 15)

if __name__ == "__main__":
    unittest.main(verbosity=2)