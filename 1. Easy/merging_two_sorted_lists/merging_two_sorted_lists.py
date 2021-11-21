'''
Given two sorted lists of integers, merge them into one large sorted list.
'''

#Binary Search - Your code took 1 millisecond — faster than 99.93% in Python

def merging_two_sorted_lists(lst0, lst1):
    for n in lst1:
        lst0.append(n)
    return sorted(lst0)