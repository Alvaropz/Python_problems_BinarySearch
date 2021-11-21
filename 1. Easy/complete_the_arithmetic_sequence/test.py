import unittest

from complete_the_arithmetic_sequence import complete_the_arithmetic_sequence

class TestCases(unittest.TestCase):
    def test_complete_the_arithmetic_sequence(self):
        self.assertEqual(complete_the_arithmetic_sequence([1,3,5,9]), 7)
        self.assertEqual(complete_the_arithmetic_sequence([0,0,0,0]), 0)
        self.assertEqual(complete_the_arithmetic_sequence([9,9,9]), 9)
        self.assertEqual(complete_the_arithmetic_sequence([12,24,36,48,72]), 60)
        self.assertEqual(complete_the_arithmetic_sequence([-3,-1,0]), -2)
        self.assertEqual(complete_the_arithmetic_sequence([-4,-3,-2,-1,0,1,2,4]), 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)