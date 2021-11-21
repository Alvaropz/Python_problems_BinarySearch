import unittest

from rotate_by_ninety_degrees_counter_clockwise import rotate_by_ninety_degrees_counter_clockwise_append, rotate_by_ninety_degrees_counter_clockwise_insert

class TestCases(unittest.TestCase):
    def test_rotate_by_ninety_degrees_counter_clockwise_append(self):
        self.assertEqual(rotate_by_ninety_degrees_counter_clockwise_append([[1,2,3],[4,5,6],[7,8,9]]), [[3, 6, 9], [2, 5, 8], [1, 4, 7]])
        self.assertEqual(rotate_by_ninety_degrees_counter_clockwise_append([[1,4,6],[8,9,8],[3,0,1]]), [[6, 8, 1], [4, 9, 0], [1, 8, 3]])
        self.assertEqual(rotate_by_ninety_degrees_counter_clockwise_append([[1,2,3,7],[4,5,6,1],[7,8,9,12],[8,5,6,1]]), [[7, 1, 12, 1], [3, 6, 9, 6], [2, 5, 8, 5], [1, 4, 7, 8]])
    
    def test_rotate_by_ninety_degrees_counter_clockwise_insert(self):
        self.assertEqual(rotate_by_ninety_degrees_counter_clockwise_insert([[1,2,3],[4,5,6],[7,8,9]]), [[3, 6, 9], [2, 5, 8], [1, 4, 7]])
        self.assertEqual(rotate_by_ninety_degrees_counter_clockwise_insert([[1,4,6],[8,9,8],[3,0,1]]), [[6, 8, 1], [4, 9, 0], [1, 8, 3]])
        self.assertEqual(rotate_by_ninety_degrees_counter_clockwise_insert([[1,2,3,7],[4,5,6,1],[7,8,9,12],[8,5,6,1]]), [[7, 1, 12, 1], [3, 6, 9, 6], [2, 5, 8, 5], [1, 4, 7, 8]])


if __name__ == "__main__":
    unittest.main(verbosity=2)