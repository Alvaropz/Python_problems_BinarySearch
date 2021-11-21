import unittest

from robinhood import robinhood

class TestCases(unittest.TestCase):
    def test_robinhood(self):
        self.assertEqual(robinhood(100, 20, 10, 130), 2)
        self.assertEqual(robinhood(2452, 56, 470, 12312312), 8)
        self.assertEqual(robinhood(100, 12, 37, 99), 0)
        self.assertEqual(robinhood(1, 1, 2, 100), 310)
        self.assertEqual(robinhood(17, 25, 50, 1000000), 36)

if __name__ == "__main__":
    unittest.main(verbosity=2)