import unittest

from verify_max_heap import verify_max_heap

class TestCases(unittest.TestCase):
    def test_verify_max_heap(self):
        self.assertEqual(verify_max_heap([4,2,3,0,1]), True)
        self.assertEqual(verify_max_heap([4,2,3,0,1]), True)
        self.assertEqual(verify_max_heap([1,2,3,0,1]), False)
        self.assertEqual(verify_max_heap([0,1]), False)
        self.assertEqual(verify_max_heap([1,2]), False)
        self.assertEqual(verify_max_heap([0,0,2]), False)
        self.assertEqual(verify_max_heap([2,0,0]), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)