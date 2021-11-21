'''
You are given a sorted and disjoint list of intervals and a list cut, which also represents an interval. 

Remove all parts of intervals that are intersecting with cut interval, and return the new list.
'''

# Binary Search - Your code took 46 milliseconds — faster than 8.28% in Python.

def interval_carving(intervals, cut):
    i = 0
    j = len(intervals)
    while i < j:
        if intervals[i][0] >= cut[0] and intervals[i][1] <= cut[1]:
            intervals.pop(i)
            i -= 1
            j -= 1
            if not intervals:
                return []
        if intervals[i][0] < cut[0] and intervals[i][1] > cut[1]:
            intervals.insert(i+1, [cut[1], intervals[i][1]])
            if cut[0] < cut[1]:
                intervals[i][1] = cut[0]
            else:
                intervals[i][1] = cut[1]
            i += 1
            j += 1
        if intervals[i][0] < cut[0] and intervals[i][1] > cut[0]:
            intervals[i][1] = cut[0]
        if intervals[i][0] >= cut[0] and intervals[i][0] < cut[1]:
            intervals[i][0] = cut[1]
        i += 1
    return intervals