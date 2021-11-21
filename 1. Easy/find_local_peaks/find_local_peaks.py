'''
You are given a list of integers nums. Return the index of every peak in the list, sorted in ascending order. An index i is called a peak if:

nums[i] > nums[i + 1] if i = 0
nums[i] > nums[i - 1] if i = n - 1
nums[i - 1] < nums[i] > nums[i + 1] otherwise
However, a list of length 1 is not considered a peak.

'''

# Binary Search - Your code took 68 milliseconds — faster than 12.07% in Python.

def find_local_peaks(nums):
    n = len(nums)
    l = []
    if n <= 1:
        return []
    for i in range(n):
        if (i == 0 and nums[i] > nums[i + 1]) or (i == n - 1 and nums[i] > nums[i - 1]) or (nums[i - 1] < nums[i] > nums[i + 1]):
            l.append(i)
    return l