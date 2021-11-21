import unittest

from strictly_alternating_list import strictly_alternating_list

class TestCases(unittest.TestCase):
    def test_strictly_alternating_list(self):
        self.assertEqual(strictly_alternating_list([1, 2, 5, 7, 4, 1, 6, 8, 3, 2]), True)
        self.assertEqual(strictly_alternating_list([1, 1, 2, 3, 2, 1]), False)
        self.assertEqual(strictly_alternating_list([1,3,5,7]), True)
        self.assertEqual(strictly_alternating_list([5, 3, 1, 5, 7]), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)