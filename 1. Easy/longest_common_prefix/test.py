import unittest

from longest_common_prefix import longest_common_prefix, longest_common_prefix_v2

class TestCases(unittest.TestCase):
    def test_longest_common_prefix(self):
        self.assertEqual(longest_common_prefix(["anthony", "ant", "antigravity"]), "ant")
        self.assertEqual(longest_common_prefix(["cow", "cowboy", "coward", "coworker"]), "cow")
        self.assertEqual(longest_common_prefix(["though", "through", "therefore", "then", "that", "there"]), "th")

    def test_longest_common_prefix_v2(self):
        self.assertEqual(longest_common_prefix_v2(["anthony", "ant", "antigravity"]), "ant")
        self.assertEqual(longest_common_prefix_v2(["cow", "cowboy", "coward", "coworker"]), "cow")
        self.assertEqual(longest_common_prefix_v2(["yet", "yell", "yeast", "yearn"]), "ye")
        self.assertEqual(longest_common_prefix_v2(["though", "through", "therefore", "then", "that", "there"]), "th")

if __name__ == "__main__":
    unittest.main(verbosity=2)