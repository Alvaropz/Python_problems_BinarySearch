'''
You are given a two-dimensional list of integers intervals where each element is an inclusive interval [start, end]. 

Return whether there's an interval which contains another interval.

intervals = [
    [1, 3],
    [4, 10],
    [4, 8],
    [9, 9]
]

True
'''

# Binary Search - Your code took 162 milliseconds — faster than 72.18% in Python.

def contained_interval(intervals):
    if len(intervals) > 1:
        srt_l = list(sorted(intervals, key=lambda item: (item[0], item[1])))
        i = 1
        j = len(intervals)
        while i < j:
            if srt_l[i][0] == srt_l[i-1][0] and srt_l[i][1] >= srt_l[i-1][1]:
                return True
            if srt_l[i][0] > srt_l[i-1][0] and srt_l[i][1] <= srt_l[i-1][1]:
                return True
            i += 1
    return False