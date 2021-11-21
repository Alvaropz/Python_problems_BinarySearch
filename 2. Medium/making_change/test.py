import unittest

from making_change import making_change_v_one, making_change_v_two

class TestCases(unittest.TestCase):
    def test_making_change_v_one(self):
        self.assertEqual(making_change_v_one(1), 1)
        self.assertEqual(making_change_v_one(2), 2)
        self.assertEqual(making_change_v_one(3), 3)
        self.assertEqual(making_change_v_one(4), 4)
        self.assertEqual(making_change_v_one(5), 1)
        self.assertEqual(making_change_v_one(6), 2)
        self.assertEqual(making_change_v_one(7), 3)
        self.assertEqual(making_change_v_one(10), 1)
        self.assertEqual(making_change_v_one(11), 2)
        self.assertEqual(making_change_v_one(16), 3)
        self.assertEqual(making_change_v_one(21), 3)
        self.assertEqual(making_change_v_one(25), 1)
        self.assertEqual(making_change_v_one(26), 2)
        self.assertEqual(making_change_v_one(31), 3)
        self.assertEqual(making_change_v_one(57), 5)
        self.assertEqual(making_change_v_one(912), 39)
        self.assertEqual(making_change_v_one(1309), 57)
        self.assertEqual(making_change_v_one(876479632), 35059188)

    def test_making_change_v_two(self):
        self.assertEqual(making_change_v_two(1), 1)
        self.assertEqual(making_change_v_two(2), 2)
        self.assertEqual(making_change_v_two(3), 3)
        self.assertEqual(making_change_v_two(4), 4)
        self.assertEqual(making_change_v_two(5), 1)
        self.assertEqual(making_change_v_two(6), 2)
        self.assertEqual(making_change_v_two(7), 3)
        self.assertEqual(making_change_v_two(10), 1)
        self.assertEqual(making_change_v_two(11), 2)
        self.assertEqual(making_change_v_two(16), 3)
        self.assertEqual(making_change_v_two(21), 3)
        self.assertEqual(making_change_v_two(25), 1)
        self.assertEqual(making_change_v_two(26), 2)
        self.assertEqual(making_change_v_two(31), 3)
        self.assertEqual(making_change_v_two(57), 5)
        self.assertEqual(making_change_v_two(912), 39)
        self.assertEqual(making_change_v_two(1309), 57)
        self.assertEqual(making_change_v_two(876479632), 35059188)


if __name__ == "__main__":
    unittest.main(verbosity=2)