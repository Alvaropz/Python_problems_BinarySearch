import unittest

from wolf_of_Wall_Street import wolf_of_wall_street, wolf_of_wall_street_less_optimed, wolf_of_wall_street_time_limit_exceeded, wolf_of_wall_street_time_limit_exceeded_two, wolf_of_wall_street_time_limit_exceeded_three

class TestCases(unittest.TestCase):
    def test_wolf_of_wall_street(self):
        self.assertEqual(wolf_of_wall_street([9, 11, 8, 5, 7, 10]), 5)
        self.assertEqual(wolf_of_wall_street([1, 2, 3, 4, 5, 6, 7, 8, 9]), 8)
        self.assertEqual(wolf_of_wall_street([9, 8, 7, 6, 5, 4, 3, 2, 1] ), 0)
        self.assertEqual(wolf_of_wall_street([9, 11, 8, 24, 4, 7, 10]), 16)
        self.assertEqual(wolf_of_wall_street([27, 82, 71, 53, 69, 56, 11, 53, 28, 0]), 55)
        self.assertEqual(wolf_of_wall_street([84, 54, 81, 35, 82, 31, 8, 23, 63, 84]), 76)

    def test_wolf_of_wall_street_less_optimised(self):
        self.assertEqual(wolf_of_wall_street_less_optimed([9, 11, 8, 5, 7, 10]), 5)
        self.assertEqual(wolf_of_wall_street_less_optimed([1, 2, 3, 4, 5, 6, 7, 8, 9]), 8)
        self.assertEqual(wolf_of_wall_street_less_optimed([9, 8, 7, 6, 5, 4, 3, 2, 1] ), 0)
        self.assertEqual(wolf_of_wall_street_less_optimed([9, 11, 8, 24, 4, 7, 10]), 16)
        self.assertEqual(wolf_of_wall_street_less_optimed([27, 82, 71, 53, 69, 56, 11, 53, 28, 0]), 55)
        self.assertEqual(wolf_of_wall_street_less_optimed([84, 54, 81, 35, 82, 31, 8, 23, 63, 84]), 76)

if __name__ == "__main__":
    unittest.main(verbosity=2)