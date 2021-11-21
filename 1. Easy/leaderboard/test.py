import unittest

from leaderboard import leaderboard

class TestCases(unittest.TestCase):
    def test_leaderboard(self):
        self.assertEqual(leaderboard([50,30,50,90,10]), [1, 2, 1, 0, 3])
        self.assertEqual(leaderboard([50,30,50]), [0, 1, 0])
        self.assertEqual(leaderboard([]), [])
        self.assertEqual(leaderboard([1,0,1]), [0, 1, 0])
        self.assertEqual(leaderboard([0]), [0])
        self.assertEqual(leaderboard([0,2,1]), [2,0,1])
        self.assertEqual(leaderboard([0,2,1,3,7,6,8,5,9,10,4]), [10, 8, 9, 7, 3, 4, 2, 5, 1, 0, 6])

if __name__ == "__main__":
    unittest.main(verbosity=2)