import unittest

from smallest_number_with_no_adjacent_duplicates import smallest_number_with_no_adjacent_duplicates

class TestCases(unittest.TestCase):
    def test_smallest_number_with_no_adjacent_duplicates(self):
        self.assertEqual(smallest_number_with_no_adjacent_duplicates("3?2??"), '31212')
        self.assertEqual(smallest_number_with_no_adjacent_duplicates("?12??"), '21212')
        self.assertEqual(smallest_number_with_no_adjacent_duplicates("3?21?"), '31212')
        self.assertEqual(smallest_number_with_no_adjacent_duplicates("???"), '121')
        self.assertEqual(smallest_number_with_no_adjacent_duplicates("?"), '1')


if __name__ == "__main__":
    unittest.main(verbosity=2)