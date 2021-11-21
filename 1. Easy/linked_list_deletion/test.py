import unittest

from linked_list_deletion import Solution, LinkedList

class TestCases(unittest.TestCase):
    def checkerMethod(self, regularList, expected, target):
        # This create two linked list, one with the given array to check and one for the expected result.
        newLinkedList = LinkedList().createFullLinkedList(regularList)
        resultLinkedList = LinkedList().createFullLinkedList(expected)
        # This filters the given array against the given target and it should return a linked list without the target in it.
        filteredLinkedList = Solution.solve(self, newLinkedList, target)
        # Lastly, it checks if both linked lists are the same. The expected result should be always True, if they are not, the solve method is wrongly coded.
        result = Solution.areIdentical(self, filteredLinkedList, resultLinkedList)
        self.assertEqual(result, True)
    
    def test_linked_list_deletion(self):
        regularList = [0, 1, 1, 2]
        expected = [0, 2]
        target = 1
        TestCases.checkerMethod(self, regularList, expected, target)
        
        regularList = [8, 6, 8, 3, 1, 2, 4, 5, 7, 8]
        expected = [6, 3, 1, 2, 4, 5, 7]
        target = 8
        TestCases.checkerMethod(self, regularList, expected, target)


if __name__ == "__main__":
    unittest.main(verbosity=2)