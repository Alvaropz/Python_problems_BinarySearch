'''
Given a singly linked list node, return its length. The linked list has fields next and val.
'''

# Binary Search - Your code took 21 milliseconds — faster than 9.35% in Python.

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

def length_of_a_linked_list(node):
    length = 0
    while node:
        node = node.next
        length += 1
    return length