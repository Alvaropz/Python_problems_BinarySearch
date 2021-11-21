import unittest

from interval_union import interval_union

class TestCases(unittest.TestCase):
    def test_interval_union(self):
        self.assertEqual(interval_union([[0,5],[4,6]]), [[0,6]])
        self.assertEqual(interval_union([[0,5],[6,7]]), [[0,5],[6,7]])
        self.assertEqual(interval_union([[6,7],[0,5]]), [[0,5],[6,7]])
        self.assertEqual(interval_union([[4,5],[3,5],[1,2]]), [[1,2],[3,5]])
        self.assertEqual(interval_union([[1,9],[4,7]]), [[1,9]])
        self.assertEqual(interval_union([[1,5]]), [[1,5]])
        self.assertEqual(interval_union([[1,5],[8,9],[15,23],[14,21],[17,31],[23,27]]), [[1, 5], [8, 9], [14, 31]])

if __name__ == "__main__":
    unittest.main(verbosity=2)