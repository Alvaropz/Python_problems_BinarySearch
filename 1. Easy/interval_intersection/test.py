import unittest

from interval_intersection import interval_intersection

class TestCases(unittest.TestCase):
    def test_interval_intersection(self):
        self.assertEqual(interval_intersection([[1,100],[10,50],[15,65]]), [15, 50])
        self.assertEqual(interval_intersection([[23,50],[12,76],[34,89]]), [34, 50])
        self.assertEqual(interval_intersection([[0,0],[1,1],[2,2]]), [2, 0])
        self.assertEqual(interval_intersection([[0,78],[14,99],[200,217],[76,1348]]), [200, 78])
        self.assertEqual(interval_intersection([[0,78],[14,99],[17,217],[12,1348]]), [17, 78])

if __name__ == "__main__":
    unittest.main(verbosity=2)