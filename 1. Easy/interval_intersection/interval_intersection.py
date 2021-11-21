'''
Given a two-dimensional integer list intervals of the form [start, end] representing intervals (inclusive), return their intersection, that is, the interval that lies within all of the given intervals.

You can assume that the intersection will be non-empty.
'''

# Binary Search - Your code took 3 milliseconds — faster than 97.25% in Python.

def interval_intersection(intervals):
    min_sub_list = max([sub_list[0] for sub_list in intervals])
    max_sub_list = min([sub_list[1] for sub_list in intervals])
    return [min_sub_list, max_sub_list]