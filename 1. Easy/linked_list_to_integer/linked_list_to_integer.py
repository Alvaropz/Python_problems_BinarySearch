'''
Given a single linked list node, representing a binary number with most significant digits first, return it as an integer.

For instance: 1 --> 0 --> 0, is the equivalent to "4" in decimal numbers.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

def linked_list_to_integer( node):
    string_binary = ""
    while node.next:
        string_binary += str(node.val)
        node.val = node.next.val
        node.next = node.next.next
    string_binary += str(node.val)
    return int(string_binary, 2)