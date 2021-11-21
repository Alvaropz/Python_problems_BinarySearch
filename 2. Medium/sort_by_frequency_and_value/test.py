import unittest

from sort_by_frequency_and_value import sort_by_frequency_and_value

class TestCases(unittest.TestCase):
    def test_sort_by_frequency_and_value(self):
        self.assertEqual(sort_by_frequency_and_value([1, 1, 5, 5, 5, 2, 2, 2, 1, 1]), [1, 1, 1, 1, 5, 5, 5, 2, 2, 2])
        self.assertEqual(sort_by_frequency_and_value([2, 3, 1, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(sort_by_frequency_and_value([1]), [1])
        self.assertEqual(sort_by_frequency_and_value([0, 1, 0]), [0, 0, 1])
        self.assertEqual(sort_by_frequency_and_value([0, 1]), [1, 0])


if __name__ == "__main__":
    unittest.main(verbosity=2)