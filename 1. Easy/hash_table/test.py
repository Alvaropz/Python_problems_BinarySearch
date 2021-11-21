import unittest

from hash_table import HashTable

class TestCases(unittest.TestCase):
    def test_hash_table(self):
        hash_table = HashTable()
        methods = ["constructor", "put", "get", "remove", "get", "put", "put", "put", "put", "put", "put", "get", "get", "put", "remove", "get", "put", "put", "get", "put", "put"]
        arguments = [[], [1, 10], [1], [1], [1], [2, 10], [2, 20], [1, 10], [3, 10], [4, 10], [3, 20], [3], [1], [4, 20], [3], [3], [3, 10], [3, 20], [4], [3, 30], [3, 40]]
        for index, method in enumerate(methods):
            if method == "constructor":
                hash_table.__init__()
            elif method == "put":
                hash_table.put(arguments[index][0], arguments[index][1])
            elif method == "get":
                hash_table.get(arguments[index][0])
            elif method == "remove":
                hash_table.remove(arguments[index][0])
        hash_table.print_hash_table()
        self.assertEqual(hash_table.list_arguments, [None, None, 10, None, -1, None, None, None, None, None, None, 20, 10, None, None, -1, None, None, 20, None, None])

if __name__ == "__main__":
    unittest.main(verbosity=2)