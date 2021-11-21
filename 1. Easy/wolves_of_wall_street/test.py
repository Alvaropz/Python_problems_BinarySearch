import unittest

from wolves_of_wall_street import wolves_of_wall_street, wolves_of_wall_street_optimised

class TestCases(unittest.TestCase):
    def test_wolves_of_wall_street(self):
        self.assertEqual(wolves_of_wall_street([1, 5, 3, 4, 6]), 7)
        self.assertEqual(wolves_of_wall_street([1, 1]), 0)
        self.assertEqual(wolves_of_wall_street([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 9)
        self.assertEqual(wolves_of_wall_street([9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)
        self.assertEqual(wolves_of_wall_street([1, 10, 10, 1, 1, 2, 5, 1, 6, 6, 6, 6]), 18)
        self.assertEqual(wolves_of_wall_street([17, 15, 137, 8, 8, 11, 43, 12, 15]), 160)
        self.assertEqual(wolves_of_wall_street([90, 123, 151, 62, 72, 73, 62, 7, 1, 43, 61, 46, 12, 18, 48, 45, 51, 32, 63, 71]), 213)

if __name__ == "__main__":
    unittest.main(verbosity=2)