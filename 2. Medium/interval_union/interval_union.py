'''
Given a two-dimensional integer list intervals representing unsorted inclusive intervals, return their union in sorted order.

Constraints:
n ≤ 100,000 where n is the length of intervals
'''

# Binary Search - Your code took 149 milliseconds — faster than 73.46% in Python.

def interval_union(intervals):
    intervals.sort()
    matrix = [intervals[0]]
    for interval in range(1, len(intervals)):
        first_current_interval = intervals[interval][0]
        last_current_interval = intervals[interval][1]
        first_matrix = matrix[-1][0]
        last_matrix = matrix[-1][1]
        if first_current_interval >= first_matrix and first_current_interval <= last_matrix and last_current_interval >= last_matrix:
            matrix[-1][1] = last_current_interval
        elif first_current_interval >= first_matrix and last_current_interval >= last_matrix:
            matrix.append(intervals[interval])
    return matrix