'''
Given a list of integers nums and an integer k, return true if you can remove exactly one element from the list to make the average equal to exactly k.

Constrains: 2 ≤ n ≤ 1,000 where n is length of nums
'''

# Binary Search - Your code took 4 milliseconds — faster than 92.22% in Python

def just_average(nums, k):
    total_sum_list = sum(nums)
    len_list_minus_one = len(nums)-1
    for number in nums:
        if (total_sum_list - number) / len_list_minus_one == k:
            return True
    return False
