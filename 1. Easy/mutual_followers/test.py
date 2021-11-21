import unittest

from mutual_followers import mutual_followers

class TestCases(unittest.TestCase):
    def test_mutual_followers(self):
        self.assertEqual(mutual_followers([[0,1],[2,3],[3,4],[1,0]]), [0,1])
        self.assertEqual(mutual_followers([[0,1],[1,2],[2,3],[3,0]]), [])
        self.assertEqual(mutual_followers([[0,1],[2,3],[3,4],[1,0],[3,2],[4,3],[3,5]]), [0, 1, 2, 3, 4])
        self.assertEqual(mutual_followers([[0,1],[2,3],[3,4],[1,0],[3,2],[4,3],[3,5],[5,3],[5,1],[5,2]]), [0, 1, 2, 3, 4, 5] )
        self.assertEqual(mutual_followers([[0,1],[0,2],[0,3],[0,4],[0,5]]), [])
        

if __name__ == "__main__":
    unittest.main(verbosity=2)