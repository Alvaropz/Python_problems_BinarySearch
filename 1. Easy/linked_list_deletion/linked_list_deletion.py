'''
Given a singly linked list node, and an integer target, return the same linked list with all nodes whose value is target removed.
'''

# Binary Search - Your code took 628 milliseconds — faster than 5.91% in Python.

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.linkedListHead = LLNode(None, None)
        self.linkedListTail = self.linkedListHead

    def createFullLinkedList(self, regularList):
        if regularList:
            self.linkedListHead = LLNode(regularList[0])
            self.linkedListTail = self.linkedListHead
            for i in range(1, len(regularList)):
                newNode = LLNode(regularList[i], None)
                self.linkedListTail.next = newNode
                self.linkedListTail = newNode
        return self.linkedListHead
    
class Solution:
    def solve(self, node, target):
        if node:
            self.head = LLNode(None)
            self.tail = self.head
        else:
            return None
        while node:
            if node.val != target:
                if self.tail.val != None:
                    newNode = LLNode(node.val)
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    self.head = LLNode(node.val)
                    self.tail = self.head
            node = node.next
        if self.head.val == None:
            return None
        return self.head

    def areIdentical(self, ownLL, expectedLL):
        a = ownLL
        b = expectedLL
        while (a != None and b != None):
            if (a.val != b.val):
                return False
            a = a.next
            b = b.next
        return (a == None and b == None)