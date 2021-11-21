import unittest

from longest_consecutive_sequence import longest_consecutive_sequence

class TestCases(unittest.TestCase):
    def test_longest_consecutive_sequence(self):
        self.assertEqual(longest_consecutive_sequence([100,4,200,1,3,2]), 4)
        self.assertEqual(longest_consecutive_sequence([1,0,2,1]), 3)
        self.assertEqual(longest_consecutive_sequence([400,300,200,100]), 1)
        self.assertEqual(longest_consecutive_sequence([0, 1]), 2)
        self.assertEqual(longest_consecutive_sequence([]), 0)
        self.assertEqual(longest_consecutive_sequence([3]), 1)
        self.assertEqual(longest_consecutive_sequence([100,4,200,1,3,2,101,105,103,102,104]), 6)
        self.assertEqual(longest_consecutive_sequence([90, 92, 94, 96, 98, 100, 102]), 1)
        self.assertEqual(longest_consecutive_sequence([77, 78, 91, 94, 93, 100, 97, 95, 96, 92, 99, 100, 98]), 10)

if __name__ == "__main__":
    unittest.main(verbosity=2)