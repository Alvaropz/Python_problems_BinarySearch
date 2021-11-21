import unittest

from lone_integer import lone_integer, lone_integer_filter

class TestCases(unittest.TestCase):
    def test_lone_integer(self):
        self.assertEqual(lone_integer([0]), 0)
        self.assertEqual(lone_integer([0,0,0,1,2,2,2]), 1)
        self.assertEqual(lone_integer([2,2,2,5]), 5)
        self.assertEqual(lone_integer([24,12,12,15]), 24)
        self.assertEqual(lone_integer([4,4,4,7,7,7,2]), 2)
        self.assertEqual(lone_integer([13,1,1,1,2,2,2,9,9,9]), 13)

    def test_lone_integer_filter(self):
        self.assertEqual(lone_integer_filter([0]), 0)
        self.assertEqual(lone_integer_filter([0,0,0,1,2,2,2]), 1)
        self.assertEqual(lone_integer_filter([2,2,2,5]), 5)
        self.assertEqual(lone_integer_filter([24,12,12,15]), 24)
        self.assertEqual(lone_integer_filter([4,4,4,7,7,7,2]), 2)
        self.assertEqual(lone_integer_filter([13,1,1,1,2,2,2,9,9,9]), 13)

if __name__ == "__main__":
    unittest.main(verbosity=2)