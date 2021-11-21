'''
You are given a list of integers nums. Consider an operation where we select some subset of integers in the list and increment all of them by one.

Return the minimum number of operations needed to make all values in the list equal to each other.

Constraints:

1 ≤ n ≤ 100,000 where n is the length of nums
0 ≤ nums[i] ≤ 10**9 for all 0 ≤ i < n
'''

# Binary Search - Your code took 17 milliseconds — faster than 93.18% in Python.

def making_list_values_equals(nums):
    return max(nums) - min(nums)