import unittest

from minimum_stack import MinimumStack

class TestCases(unittest.TestCase):

    def test(self):
        def test_function(methods, arguments):
            output = []
            for i, method in enumerate(methods):
                if method == "constructor":
                    retrievedList = MinimumStack()
                    output.append(None)
                if method == "append":
                    retrievedList.append(arguments[i][0])
                    output.append(None)
                if method == "min":
                    output.append(retrievedList.min())
                if method == "peek":
                    output.append(retrievedList.peek())
                if method == "pop":
                    output.append(retrievedList.pop())
            return output

        methods = ["constructor","append","append","min","peek","pop","pop"]
        arguments = [[],[1],[2],[],[],[],[]]
        output = test_function(methods, arguments)
        self.assertEqual(output, [None, None, None, 1, 2, 2, 1])
        
        methods = ["constructor","append","append","min","peek","pop","pop","append","append","append","min"]
        arguments = [[],[1],[2],[],[],[],[],[3],[4],[5],[]]
        output = test_function(methods, arguments)
        self.assertEqual(output, [None, None, None, 1, 2, 2, 1, None, None, None, 3])

        methods = ["constructor","append","append","min","peek","pop","pop","append","append","append","min","peek","pop","min"]
        arguments = [[],[1],[2],[],[],[],[],[3],[4],[5],[],[],[],[]]
        output = test_function(methods, arguments)
        self.assertEqual(output, [None, None, None, 1, 2, 2, 1, None, None, None, 3, 5, 5, 3])

if __name__ == "__main__":
    unittest.main(verbosity=2)