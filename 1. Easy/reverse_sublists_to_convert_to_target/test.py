import unittest

from reverse_sublists_to_convert_to_target import reverse_sublists_to_convert_to_target

class TestCases(unittest.TestCase):
    def test_reverse_sublists_to_convert_to_target(self):
        self.assertEqual(reverse_sublists_to_convert_to_target([1, 2, 3, 8, 9], [3, 2, 1, 9, 8]), True)
        self.assertEqual(reverse_sublists_to_convert_to_target([1, 2, 3, 8, 5], [5, 2, 1, 9, 8]), False)
        self.assertEqual(reverse_sublists_to_convert_to_target([1, 2, 4, 8, 9], [3, 2, 1, 9, 8]), False)
        self.assertEqual(reverse_sublists_to_convert_to_target([1, 2, 3, 8, 9], [1]), False)
        self.assertEqual(reverse_sublists_to_convert_to_target([1], [3, 2, 1, 9, 8]), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)