import unittest

from three_and_seven import three_and_seven

class TestCases(unittest.TestCase):
    def test_three_and_seven(self):
        self.assertEqual(three_and_seven(1), False)
        self.assertEqual(three_and_seven(2), False)
        self.assertEqual(three_and_seven(3), True)
        self.assertEqual(three_and_seven(4), False)
        self.assertEqual(three_and_seven(5), False)
        self.assertEqual(three_and_seven(6), True)
        self.assertEqual(three_and_seven(7), True)
        self.assertEqual(three_and_seven(8), False)
        self.assertEqual(three_and_seven(9), True)
        self.assertEqual(three_and_seven(10), True)
        self.assertEqual(three_and_seven(11), False)
        self.assertEqual(three_and_seven(12), True)
        self.assertEqual(three_and_seven(13), True)
        self.assertEqual(three_and_seven(14), True)
        self.assertEqual(three_and_seven(15), True)
        self.assertEqual(three_and_seven(16), True)
        self.assertEqual(three_and_seven(17), True)
        self.assertEqual(three_and_seven(18), True)
        self.assertEqual(three_and_seven(19), True)
        self.assertEqual(three_and_seven(20), True)
        self.assertEqual(three_and_seven(25), True)
        self.assertEqual(three_and_seven(27), True)
        self.assertEqual(three_and_seven(29), True)
        self.assertEqual(three_and_seven(51), True)
        self.assertEqual(three_and_seven(114), True)
        self.assertEqual(three_and_seven(1013), True)
        self.assertEqual(three_and_seven(8276), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)