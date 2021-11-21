import unittest

from run_length_decoded_iterator import RunLengthDecodedIterator

class TestCases(unittest.TestCase):
    def test_run_length_decoded_iterator(self):
        def call_functions(methods, class_iterator):
            list_returned = []
            for method in methods:
                if method == "constructor":
                    list_returned.append(None)
                if method == "next":
                    list_returned.append(class_iterator.next())
                if method == "hasnext":
                    list_returned.append(class_iterator.hasnext())
            return list_returned

        methods = ["constructor", "next", "hasnext", "next", "next", "hasnext"]
        arguments = [["2a1b"], [], [], [], [], []]
        class_iterator = RunLengthDecodedIterator(arguments[0][0])
        self.assertEqual(call_functions(methods, class_iterator), [None, "a", True, "a", "b", False])

        methods = ["constructor", "next", "hasnext", "next", "next", "hasnext"]
        arguments = [["2a2147483647b"], [], [], [], [], []]
        class_iterator = RunLengthDecodedIterator(arguments[0][0])
        self.assertEqual(call_functions(methods, class_iterator), [None, "a", True, "a", "b", True])

        methods = ["constructor", "next", "hasnext", "next", "next", "hasnext","next","next","hasnext","next","hasnext","next","next","next","next","next","hasnext"]
        arguments = [["1a2b3c4d1a"], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        class_iterator = RunLengthDecodedIterator(arguments[0][0])
        self.assertEqual(call_functions(methods, class_iterator), [None, "a", True, "b", "b", True, "c", "c", True, "c", True, "d", "d", "d", "d", "a", False])

if __name__ == "__main__":
    unittest.main(verbosity=2)