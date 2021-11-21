import unittest

from boss_fight import boss_fight

class TestCases(unittest.TestCase):

    def test_boss_fight_slow(self):
        self.assertEqual(boss_fight([0, 1, 1], [
                                            [0, 0, 0],
                                            [0, 0, 1],
                                            [0, 1, 1],
                                            [1, 1, 1]
                                        ]), [
                                            [0, 1, 1],
                                            [1, 1, 1]
                                        ])

if __name__ == "__main__":
    unittest.main(verbosity=2)