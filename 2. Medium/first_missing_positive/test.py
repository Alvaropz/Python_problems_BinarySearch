import unittest

from first_missing_positive import first_missing_positive_list, first_missing_positive_set

class TestCases(unittest.TestCase):
    def test_list(self):
        self.assertEqual(first_missing_positive_list([1]), 2)
        self.assertEqual(first_missing_positive_list([2]), 1)
        self.assertEqual(first_missing_positive_list([2, 3]), 1)
        self.assertEqual(first_missing_positive_list([-1, 3, 4, 5, 5, -2, 0]), 1)
        self.assertEqual(first_missing_positive_list([1, 2, 3]), 4)

    def test_set(self):
        self.assertEqual(first_missing_positive_set([1]), 2)
        self.assertEqual(first_missing_positive_set([2]), 1)
        self.assertEqual(first_missing_positive_list([2, 3]), 1)
        self.assertEqual(first_missing_positive_set([-1, 3, 4, 5, 5, -2, 0]), 1)
        self.assertEqual(first_missing_positive_set([1, 2, 3]), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)