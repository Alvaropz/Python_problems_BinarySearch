import unittest

from squeezed_list import squeezed_list, squeezed_list_optimised

class TestCases(unittest.TestCase):
    def test_squeezed_list(self):
        self.assertEqual(squeezed_list([1, 2, 3, 4, 5, 6]), [[1, 2, 3, 4, 5, 6], [3, 3, 4, 11], [6, 15], [21]])
        self.assertEqual(squeezed_list([1, 2, 3]), [[1, 2, 3], [6]])
        self.assertEqual(squeezed_list([1, 2, 3, 4]), [[1, 2, 3, 4], [3, 7], [10]])

    def test_squeezed_list_optimised(self):
        self.assertEqual(squeezed_list_optimised([1, 2, 3, 4, 5, 6]), [[1, 2, 3, 4, 5, 6], [3, 3, 4, 11], [6, 15], [21]])
        self.assertEqual(squeezed_list_optimised([1, 2, 3]), [[1, 2, 3], [6]])
        self.assertEqual(squeezed_list_optimised([1, 2, 3, 4]), [[1, 2, 3, 4], [3, 7], [10]])


if __name__ == "__main__":
    unittest.main(verbosity=2)