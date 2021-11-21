import unittest

from hoppable import hoppable_v_one, hoppable_v_two

class TestCases(unittest.TestCase):
    def test_hoppable_v_one(self):
        self.assertEqual(hoppable_v_one([1, 1, 0, 1]), False)
        self.assertEqual(hoppable_v_one([1, 1]), True)
        self.assertEqual(hoppable_v_one([1, 0, 0, 0]), False)
        self.assertEqual(hoppable_v_one([2, 4, 0, 1, 0]), True)
        self.assertEqual(hoppable_v_one([2, 2, 0, 1, 0]), True)
        self.assertEqual(hoppable_v_one([2, 2, 0, 0, 0]), False)
        self.assertEqual(hoppable_v_one([2, 2, 0, 0, 3]), False)
        self.assertEqual(hoppable_v_one([4, 2, 0, 1, 0]), True)
        self.assertEqual(hoppable_v_one([1, 1, 1]), True)
        self.assertEqual(hoppable_v_one([1, 0, 0]), False)
        self.assertEqual(hoppable_v_one([1, 1, 0]), True)
        self.assertEqual(hoppable_v_one([0, 1, 1]), False)
        self.assertEqual(hoppable_v_one([0, 0, 1]), False)
        self.assertEqual(hoppable_v_one([0, 1, 0]), False)
        self.assertEqual(hoppable_v_one([0, 0]), False)
        self.assertEqual(hoppable_v_one([1, 0]), True)
        self.assertEqual(hoppable_v_one([0, 1]), False)
        self.assertEqual(hoppable_v_one([0]), True)
        self.assertEqual(hoppable_v_one([1]), True)

    def test_hoppable_v_two(self):
        self.assertEqual(hoppable_v_two([1, 1, 0, 1]), False)
        self.assertEqual(hoppable_v_two([1, 1]), True)
        self.assertEqual(hoppable_v_two([1, 0, 0, 0]), False)
        self.assertEqual(hoppable_v_two([2, 4, 0, 1, 0]), True)
        self.assertEqual(hoppable_v_two([2, 2, 0, 1, 0]), True)
        self.assertEqual(hoppable_v_two([2, 2, 0, 0, 0]), False)
        self.assertEqual(hoppable_v_two([2, 2, 0, 0, 3]), False)
        self.assertEqual(hoppable_v_two([4, 2, 0, 1, 0]), True)
        self.assertEqual(hoppable_v_two([1, 1, 1]), True)
        self.assertEqual(hoppable_v_two([1, 0, 0]), False)
        self.assertEqual(hoppable_v_two([1, 1, 0]), True)
        self.assertEqual(hoppable_v_two([0, 1, 1]), False)
        self.assertEqual(hoppable_v_two([0, 0, 1]), False)
        self.assertEqual(hoppable_v_two([0, 1, 0]), False)
        self.assertEqual(hoppable_v_two([0, 0]), False)
        self.assertEqual(hoppable_v_two([1, 0]), True)
        self.assertEqual(hoppable_v_two([0, 1]), False)
        self.assertEqual(hoppable_v_two([0]), True)
        self.assertEqual(hoppable_v_two([1]), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)