import unittest

from missing_numbers_from_one_to_n import missing_numbers_from_one_to_n

class TestCases(unittest.TestCase):
    def test_missing_numbers_from_one_to_n(self):
        self.assertEqual(missing_numbers_from_one_to_n([3, 3, 1, 1, 5, 5]), [2, 4, 6])
        self.assertEqual(missing_numbers_from_one_to_n([1, 2, 3, 4, 5, 7]), [6])
        self.assertEqual(missing_numbers_from_one_to_n([1, 3, 4, 6, 7, 8, 8, 9, 10, 11, 3, 4]), [2, 5, 12])

if __name__ == "__main__":
    unittest.main(verbosity=2)