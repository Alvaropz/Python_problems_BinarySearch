import unittest

from large_to_small_sort import large_to_small_sort

class TestCases(unittest.TestCase):
    def test_large_to_small_sort(self):
        self.assertEqual(large_to_small_sort([5, 2, 9, 3]), [9, 2, 5, 3])
        self.assertEqual(large_to_small_sort([1, 1, 1, 1]), [1, 1, 1, 1])
        self.assertEqual(large_to_small_sort([1, 2, 3, 4]), [4, 1, 3, 2])

if __name__ == "__main__":
    unittest.main(verbosity=2)