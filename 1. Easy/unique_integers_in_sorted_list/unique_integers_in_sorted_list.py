'''
Given a list of sorted integers nums return the number of unique integers in the list.

Notes:

\mathcal{O}(n)O(n) is accepted but \mathcal{O}(k\log{}n)O(klogn) is encouraged.
'''

# Binary Search - Your code took 14 milliseconds — faster than 87.79% in Python.

def unique_integers_in_sorted_list(nums):
    return len(set(nums))
