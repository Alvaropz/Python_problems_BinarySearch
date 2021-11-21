import unittest

from longest_aliteration import longest_aliteration

class TestCases(unittest.TestCase):
    def test_longest_aliteration(self):
        self.assertEqual(longest_aliteration(["she", "sells", "seashells", "he", "sells", "clams"]), 3)
        self.assertEqual(longest_aliteration(["sells", "clams"]), 1)
        self.assertEqual(longest_aliteration(["clams"]), 1)
        self.assertEqual(longest_aliteration(["clams", "clue", "sea", "shore"]), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)