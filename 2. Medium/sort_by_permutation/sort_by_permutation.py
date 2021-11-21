'''
Given a list of strings lst and a list of integers p, reorder lst so that every lst[i] gets placed to p[i].

This should be done in O(1) space.
'''

# Binary Search - Your code took 196 milliseconds — faster than 5.04% in Python.

def sort_by_permutation(lst, p):
    tuple_list = []
    for element_first, element_second in zip(lst, p):
        tuple_list.append((element_second, element_first))
    tuple_list.sort()
    return [sub_tuple[1] for sub_tuple in tuple_list]