import unittest

from high_five import high_five

class TestCases(unittest.TestCase):
    def test_high_five(self):
        self.assertEqual(high_five(923), 9523)
        self.assertEqual(high_five(-234), -2345)
        self.assertEqual(high_five(-60), -560)
        self.assertEqual(high_five(1), 51)
        self.assertEqual(high_five(6), 65)

if __name__ == "__main__":
    unittest.main(verbosity=2)