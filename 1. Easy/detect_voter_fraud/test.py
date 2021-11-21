import unittest

from detect_voter_fraud import detect_voter_fraud

class TestCases(unittest.TestCase):
    def test_detect_voter_fraud(self):
        self.assertEqual(detect_voter_fraud([[3, 1],[3, 0],[3, 4],[3, 3],[3, 2]]), False)
        self.assertEqual(detect_voter_fraud([[3, 1],[3, 0],[3, 4],[3, 3],[4, 1]]), True)
        self.assertEqual(detect_voter_fraud([[3, 1],[1, 0],[2, 4],[2, 3],[3, 2]]), False)
        self.assertEqual(detect_voter_fraud([[3, 1]]), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)