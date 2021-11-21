import unittest

from furthest_from_origin import furthest_from_origin_v_one, furthest_from_origin_v_two, furthest_from_origin_optimised

class TestCases(unittest.TestCase):
    def test_furthest_from_origin_v_one(self):
        self.assertEqual(furthest_from_origin_v_one("LLRRR??"), 3)
        self.assertEqual(furthest_from_origin_v_one("L???LRRR??"), 6)
        self.assertEqual(furthest_from_origin_v_one("?"), 1)
        self.assertEqual(furthest_from_origin_v_one("L??LRRR?????"), 8)
        self.assertEqual(furthest_from_origin_v_one("L?R?R?L?R?R?L"), 7)
        self.assertEqual(furthest_from_origin_v_one("LRLRLRLRLRLRLLLRLRLLLRRRLRLRLRLRLRLRLRLRLRLLRLRLRLRLLRLRLRRRRRRRLLLLRRLRLRRLRLRLRRLRLRLRLRRL"), 2)
    
    def test_furthest_from_origin_v_two(self):
        self.assertEqual(furthest_from_origin_v_two("LLRRR??"), 3)
        self.assertEqual(furthest_from_origin_v_two("L???LRRR??"), 6)
        self.assertEqual(furthest_from_origin_v_two("?"), 1)
        self.assertEqual(furthest_from_origin_v_two("L??LRRR?????"), 8)
        self.assertEqual(furthest_from_origin_v_two("L?R?R?L?R?R?L"), 7)
        self.assertEqual(furthest_from_origin_v_two("LRLRLRLRLRLRLLLRLRLLLRRRLRLRLRLRLRLRLRLRLRLLRLRLRLRLLRLRLRRRRRRRLLLLRRLRLRRLRLRLRRLRLRLRLRRL"), 2)

    def test_furthest_from_origin_optimised(self):
        self.assertEqual(furthest_from_origin_optimised("LLRRR??"), 3)
        self.assertEqual(furthest_from_origin_optimised("L???LRRR??"), 6)
        self.assertEqual(furthest_from_origin_optimised("?"), 1)
        self.assertEqual(furthest_from_origin_optimised("L??LRRR?????"), 8)
        self.assertEqual(furthest_from_origin_optimised("L?R?R?L?R?R?L"), 7)
        self.assertEqual(furthest_from_origin_optimised("LRLRLRLRLRLRLLLRLRLLLRRRLRLRLRLRLRLRLRLRLRLLRLRLRLRLLRLRLRRRRRRRLLLLRRLRLRRLRLRLRRLRLRLRLRRL"), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)