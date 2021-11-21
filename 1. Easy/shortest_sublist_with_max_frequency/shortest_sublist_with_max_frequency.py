'''
You are given a list of integers nums. Let k be the frequency of a most frequent number in nums. 

Return the length of a shortest sublist such that the frequency of its most frequent number is also k.
'''

# Binary Search - Your code took 34 milliseconds — faster than 98.83% in Python.

from collections import Counter

def shortest_sublist_with_max_frequency(nums):
    dict_counting = Counter(nums)
    k = max(dict_counting.values())
    most_frequent = {key: val for key, val in dict_counting.items() if val == k}
    list_keys = list(most_frequent)
    range_indexes = []
    for value in list_keys:
        last_index = len(nums) - nums[::-1].index(value)
        range_indexes.append(last_index - nums.index(value))
    return min(range_indexes)

