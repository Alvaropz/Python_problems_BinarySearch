import unittest

from no_new_friends import no_new_friends

class TestCases(unittest.TestCase):
    def test_no_new_friends(self):
        self.assertEqual(no_new_friends(3, [[0, 1],[1, 2]]), True)
        self.assertEqual(no_new_friends(3, [[0, 1]]), False) #The third friend has no connections with anyone else.
        self.assertEqual(no_new_friends(2, [[0, 1]]), True)
        self.assertEqual(no_new_friends(2, []), False)
        self.assertEqual(no_new_friends(5, [[0,1],[1,2],[3,4],[4,2],[3,2],[4,0]]), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)