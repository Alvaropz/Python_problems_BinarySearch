'''
Given a list of integers nums, order nums by frequency, with most frequent values coming first. If there's a tie in frequency, higher valued numbers should come first.
'''

# Binary Search - Your code took 360 milliseconds — faster than 25.19% in Python.

from collections import Counter

def sort_by_frequency_and_value(nums):
    dict_nums = Counter(nums)
    sorted_list = []
    while True:
        if len(dict_nums) == 0:
            return sorted_list
        max_val = max(dict_nums.values())
        counting = list(dict_nums.values()).count(max_val)
        if counting < 2:
            for key, value in dict_nums.items():
                if value == max_val:
                    sorted_list.extend([key]*max_val)
                    dict_nums.pop(key)
                    break
        else:
            list_values = list(reversed(sorted([key for key, value in dict_nums.items() if value == max_val])))
            for number in list_values:
                sorted_list.extend([number]*max_val)
                dict_nums.pop(number)