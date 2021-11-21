import unittest

from stack_sequence import stack_sequence

class TestCases(unittest.TestCase):
    def test_stack_sequence(self):
        self.assertEqual(stack_sequence([0,1,4,6,8], [1,0,8,6,4]), True)
        self.assertEqual(stack_sequence([1,2,3,4], [4,1,2,3]), False)
        self.assertEqual(stack_sequence([0], [0]), True)
        self.assertEqual(stack_sequence([0, 1], [1, 0]), True)
        self.assertEqual(stack_sequence([1, 0], [0, 1]), True)
        self.assertEqual(stack_sequence([1, 0, 2], [2, 0, 1]), True)
        self.assertEqual(stack_sequence([2, 0, 1], [0, 1, 2]), True)
        self.assertEqual(stack_sequence([1, 0, 2], [0, 1, 2]), True)
        self.assertEqual(stack_sequence([1, 0, 2], [2, 1, 0]), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)