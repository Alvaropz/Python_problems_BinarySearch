'''
Given a list of integers nums, find all duplicate numbers and delete their last occurrences.
'''

# Binary Search - Your code took 299 milliseconds — faster than 44.62% in Python.

from collections import Counter

def remove_last_duplicate_entries_automatic_deletion_reversed(nums): 
    set_values = set()
    dict_track_duplicates = Counter(nums)
    reversed_nums = list(reversed(nums))
    for index, value in enumerate(reversed_nums):
        if not value in set_values and dict_track_duplicates[value] > 1:
            nums.pop(len(reversed_nums)-index-1)
            set_values.add(value)
    return nums

# Binary Search - Your code took 382 milliseconds — faster than 23.15% in Python.

def remove_last_duplicate_entries_list_index(nums):
    set_values = set()
    dict_track_duplicates = Counter(nums)
    list_indexes = []
    for index, value in reversed(list(enumerate(nums))):
        if not value in set_values and dict_track_duplicates[value] > 1:
            list_indexes.append(index)
            set_values.add(value)
    for value in list_indexes:
        del nums[value]
    return nums