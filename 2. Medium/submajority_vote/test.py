import unittest

from submajority_vote import submajority_vote

class TestCases(unittest.TestCase):
    def test_submajority_vote(self):
        self.assertEqual(submajority_vote([2,1,5,5,5,5,6,6,6,6,6]), [5, 6])
        self.assertEqual(submajority_vote([1,1,1,1,2,3]), [1])
        self.assertEqual(submajority_vote([1,2,3,4]), [])
        self.assertEqual(submajority_vote([1,1,1,2,2,3,3,4,4,4,4,4,4,4,5,5,5,5,6,6,6,5,3,5,6,7,3,6,8,4,2,4,5,6,7,1,3,2,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,4,4,4,4,4,4,4,4,4,4,4,4]), [5])
        
if __name__ == "__main__":
    unittest.main(verbosity=2)