import unittest

from steady_speed import steady_speed

class TestCases(unittest.TestCase):
    def test_steady_speed(self):
        self.assertEqual(steady_speed([0,3,6,3,0]), 5)
        self.assertEqual(steady_speed([0,3,6,5,4,3,1,7,10,13]), 4)
        self.assertEqual(steady_speed([0,3,6]), 3)
        self.assertEqual(steady_speed([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), 58)
        self.assertEqual(steady_speed([1, 14, 15, 16, 5, 6, 5, 13, 15, 16, 17, 18, 19, 20, 19, 18, 17, 17, 17, 17, 17, 17, 17, 17, 17, 7, 1, 0, 1, 2]), 9)

if __name__ == "__main__":
    unittest.main(verbosity=2)