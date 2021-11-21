import unittest

from ancient_astronaut_theory import ancient_astronaut_theory

class TestCases(unittest.TestCase):
    def test_ancient_astronaut_theory(self):
        self.assertEqual(ancient_astronaut_theory("acb", "aaaa h ccc i bbb"), True) # a < c < b. First goes a, then c, then b.
        self.assertEqual(ancient_astronaut_theory("acb", "aaaacccbc"), False) # a < c < b < c. First goes a, then c, then b but then c. Because c should be before b, this condition is False.
        self.assertEqual(ancient_astronaut_theory("bfg", "bfg"), True)
        self.assertEqual(ancient_astronaut_theory("bfg", "bfgb"), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)