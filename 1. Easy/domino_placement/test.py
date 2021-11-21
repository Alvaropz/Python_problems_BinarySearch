import unittest

from domino_placement import domino_placement

class TestCases(unittest.TestCase):
    def test(self):
        self.assertEqual(domino_placement(2, 2), 2)
        self.assertEqual(domino_placement(6, 4), 12)
        self.assertEqual(domino_placement(5, 2), 5)
        self.assertEqual(domino_placement(10, 3), 15)
        self.assertEqual(domino_placement(1161, 7197), 4177858)

if __name__ == "__main__":
    unittest.main(verbosity=2)