'''
You are given a list of integers nums and an integer k. Consider an operation where you pick an element in nums and negate it. 

Given that you must make exactly k operations, return the maximum resulting sum that can be obtained.
'''

# Binary Search - Your code took 108 milliseconds — faster than 58.11% in Python.

def largest_sum_after_k_negations(nums, k):
    if not nums:
        return 0
    nums.sort()
    i = 0
    while k > 0:
        if nums[i] >= 0 or i >= len(nums)-1:
            break
        if nums[i] < 0:
            nums[i] = abs(nums[i])
            k -= 1
            i += 1
    if k > 0 and k % 2 != 0:
        nums[nums.index(min(nums))] = nums[nums.index(min(nums))] * -1
    return sum(nums)