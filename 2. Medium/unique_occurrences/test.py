import unittest

from unique_occurrences import unique_occurrences

class TestCases(unittest.TestCase):
    def test_unique(self):
        self.assertEqual(unique_occurrences([5, 3, 1, 8, 3, 1, 1, 8, 8, 8]), True)
        self.assertEqual(unique_occurrences([5, 3, 1, 8, 3, 1, 1, 8, 8]), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)