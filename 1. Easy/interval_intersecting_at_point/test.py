import unittest

from interval_intersecting_at_point import interval_intersecting_at_point

class TestCases(unittest.TestCase):
    def test_interval_intersecting_at_point(self):
        self.assertEqual(interval_intersecting_at_point([[1,5],[3,9],[4,8],[10,13]], 4), 3)
        self.assertEqual(interval_intersecting_at_point([[1,5],[3,9],[4,8],[10,13]], 2), 1)
        self.assertEqual(interval_intersecting_at_point([[1,5],[3,9],[4,8],[10,13]], 5), 3)
        self.assertEqual(interval_intersecting_at_point([[1,5],[3,9],[4,8],[10,13]], 9), 1)
        self.assertEqual(interval_intersecting_at_point([[1,5],[3,9],[4,8],[10,13]], 1), 1)
        self.assertEqual(interval_intersecting_at_point([[1,5]], 0), 0)
        self.assertEqual(interval_intersecting_at_point([[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9]], 6), 4)
        self.assertEqual(interval_intersecting_at_point([[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9]], 2), 8)

if __name__ == "__main__":
    unittest.main(verbosity=2)