'''
Given the head of a singly linked list head, return whether the values of the nodes are sorted in a strictly increasing order.
'''

# Binary Search - our code took 93 milliseconds — faster than 10.91% in Python.

#class LLNode:
#    def __init__(self, val, next=None):
#        self.val = val
#        self.next = next

def a_strictly_increasing_linked_list(head):
    while head.next:
        if head.val < head.next.val:
            head.val = head.next.val
            head.next = head.next.next
        else:
            return False
    return True