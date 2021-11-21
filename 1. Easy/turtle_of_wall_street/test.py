import unittest

from turtle_of_wall_street import turtle_of_wall_street

class TestCases(unittest.TestCase):
    def test_turtle_of_wall_street(self):
        self.assertEqual(turtle_of_wall_street([0]), 0)
        self.assertEqual(turtle_of_wall_street([1, 0]), 0)
        self.assertEqual(turtle_of_wall_street([0, 1]), 1)
        self.assertEqual(turtle_of_wall_street([1, 2, 5, 1, 3]), 9)
        self.assertEqual(turtle_of_wall_street([5, 2]), 0)
        self.assertEqual(turtle_of_wall_street([1, 2, 3, 4, 5, 6, 7, 8]), 28)
        self.assertEqual(turtle_of_wall_street([8, 7, 6, 5, 4, 3, 2, 1]), 0)
        self.assertEqual(turtle_of_wall_street([5, 5, 5, 5, 5, 5, 5]), 0)
        self.assertEqual(turtle_of_wall_street([1, 2, 3, 4, 4, 4, 3, 2, 1]), 6)
        self.assertEqual(turtle_of_wall_street([1, 3, 4, 6, 5, 7, 2, 8]), 28)

if __name__ == "__main__":
    unittest.main(verbosity=2)