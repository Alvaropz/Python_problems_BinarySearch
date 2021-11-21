'''
You are given a singly linked list head as well as integers pos and val. Insert a new node with value val before index pos of head.
'''

# Binary Search - Your code took 70 milliseconds — faster than 7.39% in Python.

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def solve(self, head, pos, val):
        if not head:
            return None

        if pos == 0:
            self.head = LLNode(val, head)
            i = float('-inf')
        else:
            self.head = head
            i = 0
        
        self.tail = self.head
        length = 0

        while head:
            if i+1 == pos:
                self.tail.next = LLNode(val, head.next)
                self.tail = self.tail.next
            else:
                if self.tail.next:
                    self.tail = self.tail.next
                head = head.next
                length += 1
            i += 1
        if i == length:
            self.tail.next = LLNode(val)
        return self.head