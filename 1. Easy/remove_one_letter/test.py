import unittest

from remove_one_letter import remove_one_letter

class TestCases(unittest.TestCase):
    def test_remove_one_letter(self):
        self.assertEqual(remove_one_letter("hello", "helo"), True)
        self.assertEqual(remove_one_letter("hello", "hello"), False)
        self.assertEqual(remove_one_letter("ca", "c"), True)
        self.assertEqual(remove_one_letter("house", "home"), False)
        self.assertEqual(remove_one_letter("mug", "mu"), True)
        self.assertEqual(remove_one_letter("book", "ook"), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)