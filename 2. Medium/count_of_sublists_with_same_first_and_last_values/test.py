import unittest

from count_of_sublists_with_same_first_and_last_values import count_of_sublists_with_same_first_and_last_values

class TestCases(unittest.TestCase):
    def test_count_of_sublists_with_same_first_and_last_values(self):
        self.assertEqual(count_of_sublists_with_same_first_and_last_values([1,5,3,1]), 5)
        self.assertEqual(count_of_sublists_with_same_first_and_last_values([1,5,3,1,1,1,1,1,2]), 24)
        self.assertEqual(count_of_sublists_with_same_first_and_last_values([1,5,3,1,1,5,3,1,5,1,3]), 27)
        self.assertEqual(count_of_sublists_with_same_first_and_last_values([1,5,3,1,5,6,7,8,9,10,11,12]), 14)
        self.assertEqual(count_of_sublists_with_same_first_and_last_values([1]), 1)
        self.assertEqual(count_of_sublists_with_same_first_and_last_values([1,5]), 2)
        self.assertEqual(count_of_sublists_with_same_first_and_last_values([1,5,1]), 4)
        self.assertEqual(count_of_sublists_with_same_first_and_last_values([1,5,3,1,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), 22)

if __name__ == "__main__":
    unittest.main(verbosity=2)