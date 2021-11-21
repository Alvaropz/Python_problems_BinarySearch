'''
You are given a list of integers nums that used to be an arithmetic sequence. 

Given that a number was removed, and that the number was not the first or the last element, return the removed number.
'''

# Binary Search - Your code took 349 milliseconds — faster than 3.26% in Python.

def complete_the_arithmetic_sequence(nums):
    if sum(nums) / len(nums) == nums[0]:
        return nums[0]
    if len(nums) == 2:
        return (max(nums)+min(nums))/2
    d = {}
    new_list = []
    for i in range(1, len(nums)):
        difference = nums[i] - nums[i-1]
        new_list.append((difference, nums[i]))
        if difference in d:
            d[difference] += 1
        else:
            d[difference] = 1
    largest = [k for k, v in d.items() if v == max(d.values())][0]
    for sub_tuple in new_list:
        if sub_tuple[0] != largest:
            return sub_tuple[1] - largest