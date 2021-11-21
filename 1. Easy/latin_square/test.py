import unittest

from latin_square import latin_square

class TestCases(unittest.TestCase):
    def test_latin_square(self):
        self.assertEqual(latin_square([
                            ["a", "b", "c"],
                            ["c", "a", "b"],
                            ["b", "c", "a"]
                        ]), True)
        self.assertEqual(latin_square([
                            ["a", "b", "c"],
                            ["c", "a", "b"],
                            ["b", "c", "c"]
                        ]), False)
        self.assertEqual(latin_square([
                            ["a", "b", "c"],
                            ["d", "a", "b"],
                            ["b", "c", "a"]
                        ]), False)
        self.assertEqual(latin_square([
                            ["d", "b", "a"],
                            ["c", "a", "b"],
                            ["b", "c", "a"]
                        ]), False)
        self.assertEqual(latin_square([
                            ["a", "b", "c", "d"],
                            ["b", "a", "d", "c"],
                            ["c", "d", "a", "b"],
                            ["d", "z", "b", "a"]
                        ]), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)