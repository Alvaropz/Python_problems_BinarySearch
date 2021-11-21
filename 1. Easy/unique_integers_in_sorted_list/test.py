import unittest

from unique_integers_in_sorted_list import unique_integers_in_sorted_list

class TestCases(unittest.TestCase):
    def test_unique_integers_in_sorted_list(self):
        self.assertEqual(unique_integers_in_sorted_list([2, 2, 2, 3, 4, 6, 6]), 4)
        self.assertEqual(unique_integers_in_sorted_list([1, 2, 3, 4, 5, 6]), 6)
        self.assertEqual(unique_integers_in_sorted_list([0]), 1)
        self.assertEqual(unique_integers_in_sorted_list([1, 1, 1, 1, 1]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)