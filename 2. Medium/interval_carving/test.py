import unittest

from interval_carving import interval_carving

class TestCases(unittest.TestCase):
    def test_interval_carving(self):
        self.assertEqual(interval_carving([[1,10],[12,30],[40,60]], [7,45]), [[1, 7], [45, 60]])
        self.assertEqual(interval_carving([[3,8]], [5,5]), [[3, 5], [5, 8]])
        self.assertEqual(interval_carving([[50,90]], [38, 75]), [[75, 90]])
        self.assertEqual(interval_carving([[2,6]], [4,8]), [[2, 4]])
        self.assertEqual(interval_carving([[3,4]],[0,4]), [])

if __name__ == "__main__":
    unittest.main(verbosity=2)