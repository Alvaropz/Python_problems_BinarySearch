import unittest

from guess_the_root import guess_the_root

class TestCases(unittest.TestCase):
    def test_guess_the_root(self):
        self.assertEqual(guess_the_root(9), 3)
        self.assertEqual(guess_the_root(5), 2)
        self.assertEqual(guess_the_root(16), 4)
        self.assertEqual(guess_the_root(26), 5)
        self.assertEqual(guess_the_root(123413241), 11109)

if __name__ == "__main__":
    unittest.main(verbosity=2)