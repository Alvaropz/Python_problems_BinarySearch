import unittest

from eliminate_it import eliminate_it

class TestCases(unittest.TestCase):
    def test_eliminate_it(self):
        self.assertEqual(eliminate_it("xyxyxz"), "xx")
        self.assertEqual(eliminate_it("z"), "z")
        self.assertEqual(eliminate_it("zx"), "zx")
        self.assertEqual(eliminate_it("xy"), "x")
        self.assertEqual(eliminate_it("yx"), "x")
        self.assertEqual(eliminate_it("xzy"), "")

if __name__ == "__main__":
    unittest.main(verbosity=2)