import unittest

from connell_sequence import connell_sequence

class TestCases(unittest.TestCase):
    def test_connell_sequence(self):
        self.assertEqual(connell_sequence(1), 2)
        self.assertEqual(connell_sequence(2), 4)
        self.assertEqual(connell_sequence(3), 5)
        self.assertEqual(connell_sequence(4), 7)
        self.assertEqual(connell_sequence(5), 9)
        self.assertEqual(connell_sequence(6), 10)
        self.assertEqual(connell_sequence(7), 12)
        self.assertEqual(connell_sequence(8), 14)
        self.assertEqual(connell_sequence(9), 16)
        self.assertEqual(connell_sequence(10), 17)
        self.assertEqual(connell_sequence(11), 19)
        self.assertEqual(connell_sequence(15), 26)
        self.assertEqual(connell_sequence(19), 34)
        self.assertEqual(connell_sequence(21), 37)
        self.assertEqual(connell_sequence(32), 58)
        self.assertEqual(connell_sequence(47), 86)
        self.assertEqual(connell_sequence(51), 94)

if __name__ == "__main__":
    unittest.main(verbosity=2)