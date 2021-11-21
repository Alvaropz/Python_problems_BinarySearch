import unittest

from knights_attack import knights_attack

class TestCases(unittest.TestCase):
    def test_knights_attack(self):
        self.assertEqual(knights_attack([[0,0,1,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]), True)
        self.assertEqual(knights_attack([[0,0,0,0,0],[1,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]), True)
        self.assertEqual(knights_attack([[0,0,0,0,0],[0,0,0,0,1],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]), True)
        self.assertEqual(knights_attack([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[1,0,0,0,0],[0,0,0,0,0]]), True)
        self.assertEqual(knights_attack([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,0,0,0,0]]), True)
        self.assertEqual(knights_attack([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,1,0,0,0]]), True)
        self.assertEqual(knights_attack([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0]]), True)
        self.assertEqual(knights_attack([[0,0,0,1,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]), True)
        self.assertEqual(knights_attack([[0,1,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]), True)
        self.assertEqual(knights_attack([[0,0,0,0,1],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]), False)
        self.assertEqual(knights_attack([[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1]]), False)
        self.assertEqual(knights_attack([[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]]), False)
        self.assertEqual(knights_attack([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]), False)
        self.assertEqual(knights_attack([[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1]]), False)
        self.assertEqual(knights_attack([[1,0,0,1,1],[0,1,0,1,0],[0,1,1,0,0],[0,1,0,1,0],[1,1,0,0,1]]), True)
        self.assertEqual(knights_attack([[1,0,0,0,1],[0,1,0,1,0]]), False)
        self.assertEqual(knights_attack([[1,0,0,0,1],[0,0,0,1,1]]), False)
        self.assertEqual(knights_attack([[1,0,0,0,1],[0,1,1,1,0]]), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)