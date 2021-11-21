import unittest

from find_local_peaks import find_local_peaks

class TestCases(unittest.TestCase):
    def test(self):
        self.assertEqual(find_local_peaks([]), [])
        self.assertEqual(find_local_peaks([5]), [])
        self.assertEqual(find_local_peaks([1,5]), [1])
        self.assertEqual(find_local_peaks([5,1]), [0])
        self.assertEqual(find_local_peaks([5,1]), [0])
        self.assertEqual(find_local_peaks([5,1,3]), [0,2])
        self.assertEqual(find_local_peaks([6,7,3,4,5,7,2,8,4,6]), [1, 5, 7, 9])
        self.assertEqual(find_local_peaks([1,2,3,2,4,5,7,2,8,4,6]), [2, 6, 8, 10])
        self.assertEqual(find_local_peaks([1,2,3,2,4,5,6,7,3,4,5,7]), [2, 7, 11])
        self.assertEqual(find_local_peaks([1,2,3,2,4,5,6,7,3,8,4,6]), [2, 7, 9, 11])

if __name__ == "__main__":
    unittest.main(verbosity=2)