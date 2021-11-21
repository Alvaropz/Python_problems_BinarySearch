import unittest

from rotation_groups import rotation_groups

class TestCases(unittest.TestCase):
    def test_rotation_groups(self):
        self.assertEqual(rotation_groups(["abc", "xy", "yx", "z", "bca"]), 3)
        self.assertEqual(rotation_groups(["aaaaa", "aaaa", "aaa", "aa", "a"]), 5)
        self.assertEqual(rotation_groups(["hans", "hulke", "e", "kehul"]), 3)
        self.assertEqual(rotation_groups([]), 0)
        self.assertEqual(rotation_groups(["anununu"]), 1)
        self.assertEqual(rotation_groups(["apapa", "amama"]), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)