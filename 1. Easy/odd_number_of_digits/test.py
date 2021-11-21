import unittest

from odd_number_of_digits import odd_number_of_digits_cl, odd_number_of_digits_for

class TestCases(unittest.TestCase):
    def test_odd_number_of_digits_cl(self):
        self.assertEqual(odd_number_of_digits_cl([1, 800, 2, 10, 3]), 4)
        self.assertEqual(odd_number_of_digits_cl([10, 80, 30, 20, 40]), 0)
        self.assertEqual(odd_number_of_digits_cl([2, 2]), 2)
        self.assertEqual(odd_number_of_digits_cl([1, 22, 333, 4444, 55555]), 3)

    def test_odd_number_of_digits_for(self):
        self.assertEqual(odd_number_of_digits_for([1, 800, 2, 10, 3]), 4)
        self.assertEqual(odd_number_of_digits_for([10, 80, 30, 20, 40]), 0)
        self.assertEqual(odd_number_of_digits_for([2, 2]), 2)
        self.assertEqual(odd_number_of_digits_for([1, 22, 333, 4444, 55555]), 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)