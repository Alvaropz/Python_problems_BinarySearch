import unittest

from task_hare import task_hare

class TestCases(unittest.TestCase):
    def test_task_hare(self):
        self.assertEqual(task_hare([3, 2, 9, 13], [10, 5, 2, 1]), 3)
        self.assertEqual(task_hare([3, 2, 9, 1, 5, 7], [10, 5, 2, 1, 4, 3]), 5)
        self.assertEqual(task_hare([1, 2, 3], [4, 5, 6]), 3)
        self.assertEqual(task_hare([4, 5, 6], [1, 2, 3]), 0)
        self.assertEqual(task_hare([4, 5, 6], [1, 2, 3]), 0)
        self.assertEqual(task_hare([1], [2, 2]), 1)
        self.assertEqual(task_hare([2], [1, 1]), 0)
        self.assertEqual(task_hare([2, 1], [1, 1]), 1)
        self.assertEqual(task_hare([1, 1], [1, 1]), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)