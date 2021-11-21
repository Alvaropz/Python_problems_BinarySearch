import unittest

from unique_ab_string import unique_ab_string

class TestCases(unittest.TestCase):
    def test_unique_ab_string(self):
        self.assertEqual(unique_ab_string("abbababaaabbbaaaaa"), 2048)
        self.assertEqual(unique_ab_string("ab"), 2)
        self.assertEqual(unique_ab_string("abbababaaabbbaa"), 256)
        self.assertEqual(unique_ab_string("aaaaaaaaaaaaa"), 8192)
        self.assertEqual(unique_ab_string("bbbbbbbbbbb"), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)