'''
You are given a list of unique integers nums. 

Return a sorted two dimensional list of integers where each list represents an inclusive interval summarizing integers that are contiguous in nums.
'''

# Binary Search - Your code took 81 milliseconds — faster than 71.74% in Python.

def contiguous_interval(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return [[nums[0], nums[0]]]
    nums.sort()
    i = 1
    j = len(nums)-1
    contiguous_intervals = []
    while i <= j:
        if nums[i]-1 == nums[i-1]:
            first_number = nums[i-1]
            i += 1
            while i <= j and nums[i]-1 == nums[i-1]:
                i += 1
            last_number = nums[i-1]
            contiguous_intervals.append([first_number, last_number])
            i += 1
        else:
            contiguous_intervals.append([nums[i-1], nums[i-1]])
            i += 1
    if nums[-2]+1 != nums[-1]:
        contiguous_intervals.append([nums[-1], nums[-1]])
    return contiguous_intervals