import unittest

from roomba import roomba

class TestCases(unittest.TestCase):
    def test_roomba(self):
        self.assertEqual(roomba(["NORTH", "SOUTH", "WEST"], -1, 0), True)
        self.assertEqual(roomba(["NORTH", "EAST"], 1, 1), True)
        self.assertEqual(roomba(["NORTH", "EAST", "NORTH", "NORTH", "EAST", "WEST", "SOUTH"], 1, 2), True)
        self.assertEqual(roomba([], 0, 0), True)
        self.assertEqual(roomba([], 1295, 567), False)
        self.assertEqual(roomba(["SOUTH"], 0, 1), False)
        self.assertEqual(roomba(["WEST"], 1, 0), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)