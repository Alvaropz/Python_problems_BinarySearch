import unittest

from contiguous_interval import contiguous_interval

class TestCases(unittest.TestCase):
    def test_contiguous_interval(self):
        self.assertEqual(contiguous_interval([]), [])
        self.assertEqual(contiguous_interval([1]), [[1,1]])
        self.assertEqual(contiguous_interval([1,2]), [[1,2]])
        self.assertEqual(contiguous_interval([1,3]), [[1,1],[3,3]])
        self.assertEqual(contiguous_interval([1, 3, 2, 7, 6]), [[1, 3], [6, 7]])
        self.assertEqual(contiguous_interval([1,3,2,7,6,8,9,12,13,14,15,18,34,31,23,35]), [[1, 3], [6, 9], [12, 15], [18, 18], [23, 23], [31, 31], [34, 35]])
        self.assertEqual(contiguous_interval([1,3,2,7,6,8,9,12,13,14,15,18,34,31,23,67]), [[1, 3], [6, 9], [12, 15], [18, 18], [23, 23], [31, 31], [34, 34], [67, 67]])

if __name__ == "__main__":
    unittest.main(verbosity=2)