import unittest

from sum_of_two_numbers import sum_of_two_numbers

class TestCases(unittest.TestCase):
    def test_sum_of_two_numbers(self):
        self.assertEqual(sum_of_two_numbers([35, 8, 18, 3, 22], 11), True)
        self.assertEqual(sum_of_two_numbers([35, 0, 18, 11, 22], 11), True)
        self.assertEqual(sum_of_two_numbers([1, 0, 3, 4, 5], 11), False)
        self.assertEqual(sum_of_two_numbers([-11, -22, 11, 22], 0), True)
        self.assertEqual(sum_of_two_numbers([2], 4), False)
        self.assertEqual(sum_of_two_numbers([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4], 5), True)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)