import unittest

from remove_last_duplicate_entries import remove_last_duplicate_entries_automatic_deletion_reversed, remove_last_duplicate_entries_list_index

class TestCases(unittest.TestCase):
    def test_remove_last_duplicate_entries_automatic_deletion_reversed(self):
        self.assertEqual(remove_last_duplicate_entries_automatic_deletion_reversed([1,2,3,4,5]), [1,2,3,4,5])
        self.assertEqual(remove_last_duplicate_entries_automatic_deletion_reversed([1]), [1])
        self.assertEqual(remove_last_duplicate_entries_automatic_deletion_reversed([1,2,2,3,3,4,4,1]), [1,2,3,4])
        self.assertEqual(remove_last_duplicate_entries_automatic_deletion_reversed([1, 3, 4, 1, 3, 5]), [1, 3, 4, 5])

    def test_remove_last_duplicate_entries_list_index(self):
        self.assertEqual(remove_last_duplicate_entries_list_index([1,2,3,4,5]), [1,2,3,4,5])
        self.assertEqual(remove_last_duplicate_entries_list_index([1]), [1])
        self.assertEqual(remove_last_duplicate_entries_list_index([1,2,2,3,3,4,4,1]), [1,2,3,4])
        self.assertEqual(remove_last_duplicate_entries_list_index([1, 3, 4, 1, 3, 5]), [1, 3, 4, 5])

if __name__ == "__main__":
    unittest.main(verbosity=2)