import unittest

from rookie_mistake import rookie_mistake

class TestCases(unittest.TestCase):
    def test_rookie_mistake(self):
        self.assertEqual(rookie_mistake("......B....R.............."), True)
        self.assertEqual(rookie_mistake("......B....R...........B.."), False)
        self.assertEqual(rookie_mistake("B.....B....R......B....B.."), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)