'''
Given a list of integers nums, sorted in ascending order, and a number target, return the index where target should be inserted to keep nums sorted. If target already exists in nums, return the largest index where target can be inserted.

This should be done in \mathcal{O}(\log n)O(logn).
'''

# Binary Search - Your code took 132 milliseconds — faster than 1.90% in Python.

def insertion_index_in_sorted_list(nums, target):
    lenght_nums = len(nums)
    if lenght_nums == 1:
        if target >= nums[0]:
            return 1
        else:
            return 0
    if len(nums) == 2:
        if target > nums[0] and target < nums[1]:
            return 1
    nearest = min(nums, key=lambda x:abs(x-target))
    index_nearest = nums.index(nearest)
    if nearest == target:
        index_nearest = lenght_nums - nums[::-1].index(nearest) - 1
        return index_nearest+1
    else:
        if index_nearest != lenght_nums-1:
            if target < nearest:
                return index_nearest
            if target < nums[index_nearest+1]:
                return index_nearest+1
            if target > nearest:
                return lenght_nums
        else:
            if target > nearest:
                return lenght_nums