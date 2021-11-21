'''
Given an unsorted array of integers nums, find the length of the longest sequence of consecutive elements.
'''

# Binary Search - Your code took 424 milliseconds — faster than 30.21% in Python.

def longest_consecutive_sequence(nums):
    if nums:
        nums = sorted(list(dict.fromkeys(nums)))
        i = 0
        j = len(nums)-1
        longest = 1
        while i+1 <= j:
            temp_count = 0
            if nums[i]+1 == nums[i+1]:
                while i+1 <= j and nums[i]+1 == nums[i+1]:
                    temp_count += 1
                    i += 1
                temp_count += 1
                if temp_count > longest:
                    longest = temp_count
            i += 1
        return longest
    return 0