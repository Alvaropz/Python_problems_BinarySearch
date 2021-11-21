import unittest

from common_words import common_words

class TestCases(unittest.TestCase):
    def test_common_words(self):
        self.assertEqual(common_words("hello world hello oyster", "world is your oyster"), 2)
        self.assertEqual(common_words("juniper jalgo", "JuNiper JalgO"), 2)
        self.assertEqual(common_words("muffin croissant bread cake", "cake croissant engine plane wings"), 2)
        self.assertEqual(common_words("miau guau muu kikiriki oink", "brum brum"), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)