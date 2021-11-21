import unittest

from making_pizza import making_pizza

class TestCases(unittest.TestCase):
    def test_making_pizza(self):
        self.assertEqual(making_pizza("pizzapizza"), 2)
        self.assertEqual(making_pizza("pizzapizz"), 1)
        self.assertEqual(making_pizza("pizza"), 1)
        self.assertEqual(making_pizza("izizza"), 0)
        self.assertEqual(making_pizza("pizzaaaazzzzz"), 1)
        self.assertEqual(making_pizza("abcdefghijklmnopqrstuvwxyz"), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)