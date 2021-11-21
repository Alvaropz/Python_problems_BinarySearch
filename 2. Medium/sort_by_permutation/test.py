import unittest

from sort_by_permutation import sort_by_permutation

class TestCases(unittest.TestCase):
    def test_sort_by_permutation(self):
        self.assertEqual(sort_by_permutation(["a", "b", "c", "d"], [3, 0, 1, 2]), ["b", "c", "d", "a"])
        self.assertEqual(sort_by_permutation(["a", "b", "c", "d"], [0, 1, 2, 3]), ["a", "b", "c", "d"])
        self.assertEqual(sort_by_permutation(["a", "b", "c", "d"], [2, 1, 0, 3]), ["c", "b", "a", "d"])

if __name__ == "__main__":
    unittest.main(verbosity=2)