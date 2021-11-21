'''
You are given a two-dimensional list of integers intervals and an integer point. Each element contains [start, end] represents an inclusive interval.

Return the number of intervals that are intersecting at point.
'''

# Binary Search - Your code took 18 milliseconds — faster than 83.11% in Python.

def interval_intersecting_at_point(intervals, point):
    count = 0
    for sub_list in intervals:
        if sub_list[0] <= point <= sub_list[1]:
            count += 1
    return count