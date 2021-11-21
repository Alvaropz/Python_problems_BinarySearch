'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
'''

def largest_sum_non_adjacent_num(nums):
    total_n = 0
    if len(nums) % 2 == 0:
        return nums[0] + nums[-1]
    else:
        for index in range(len(nums)):
            if index % 2 == 0:
                total_n += nums[index]
    return total_n