import unittest

from triangle_stairs import triangle_stairs

class TestCases(unittest.TestCase):
    def test_triangle_stairs(self):
        self.assertEqual(triangle_stairs(4), "   *\n  **\n ***\n****")
        self.assertEqual(triangle_stairs(5), "    *\n   **\n  ***\n ****\n*****")
        self.assertEqual(triangle_stairs(3), "  *\n **\n***")
        self.assertEqual(triangle_stairs(1), "*")


if __name__ == "__main__":
    unittest.main(verbosity=2)