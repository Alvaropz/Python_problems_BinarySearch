import unittest

from in_place_move_zeros_to_end_of_list import in_place_move_zeros_to_end_of_list

class TestCases(unittest.TestCase):
    def test_in_place_move_zeros_to_end_of_list(self):
        self.assertEqual(in_place_move_zeros_to_end_of_list([0, 1, 0, 2, 3]), [1, 2, 3, 0, 0])
        self.assertEqual(in_place_move_zeros_to_end_of_list([1, 2, 3]), [1, 2, 3])
        self.assertEqual(in_place_move_zeros_to_end_of_list([0, 0]), [0, 0])
        self.assertEqual(in_place_move_zeros_to_end_of_list([0, 1, 0, 2, 3, 6, 1, 9, 0, 10, 2, 0, 0]), [1, 2, 3, 6, 1, 9, 10, 2, 0, 0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main(verbosity=2)