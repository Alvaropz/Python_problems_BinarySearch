'''
Given a list of integers nums and an integer k, return the maximum possible i where nums[0] + nums[1] + ...  + nums[i] ≤ k. Return -1 if no valid i exists.
'''

# Binary Search - Your code took 7 milliseconds — faster than 87.65% in Python.

def k_prefix(nums, k):
    list_total = []
    total = 0
    for number in nums:
        total += number
        list_total.append(total)
    list_total.reverse()
    for idx in range(len(list_total)):
        if list_total[idx] <= k:
            return len(list_total)-1-idx
    return -1