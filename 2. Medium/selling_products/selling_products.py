'''
You are given a list of integers items and an integer n. A salesperson has items in a bag with random IDs. The salesperson can remove as many as n items from the bag.

Determine the minimum number of different IDs the final bag can contain after performing, at most n deletions.
'''

# Binary Search - Your code took 564 milliseconds — faster than 0.61% in Python

from collections import Counter
import heapq

def selling_products(items, n):
    d = Counter(items)
    list_values = sorted(d.values())
    if n == 0:
        return len(list_values)
    elif not items or sum(list_values) == n:
        return 0
    if len(list_values) == 1:
        return 1
    c_value = list_values[0]
    while n > 0:
        if n - c_value >= 0:
            n -= c_value
            list_values.pop(0)
            c_value = list_values[0]
        else:
            n = 0
    return len(list_values)