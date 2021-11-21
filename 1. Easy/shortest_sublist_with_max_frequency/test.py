import unittest

from shortest_sublist_with_max_frequency import shortest_sublist_with_max_frequency

class TestCases(unittest.TestCase):
    def test_shortest_sublist_with_max_frequency(self):
        self.assertEqual(shortest_sublist_with_max_frequency([1, 2, 3, 4, 3, 1]), 3)
        self.assertEqual(shortest_sublist_with_max_frequency([1, 1, 1, 1, 1, 1]), 6)
        self.assertEqual(shortest_sublist_with_max_frequency([2, 2, 1, 6, 6, 1]), 2)
        self.assertEqual(shortest_sublist_with_max_frequency([2, 2, 1, 6, 6, 8, 4, 8, 8]), 4)
        self.assertEqual(shortest_sublist_with_max_frequency([1, 3, 1, 3, 1, 3]), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)