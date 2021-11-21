'''
You are given an integer list nums containing 0s and 1s. Consider an operation where we pick an index i in nums and flip i as well as all numbers to the right of i. 

Return the minimum number of operations required to make nums contain all 0s.
'''

# Binary Search -Your code took 20 milliseconds — faster than 100.00% in Python.

def flip_to_zeros(nums):
    if not nums:
        return 0
    count = 0
    ref_number = nums[0]
    for number in nums:
        if number != ref_number:
            count += 1
            ref_number = number
    if nums[0] == 1:
        return count + 1
    return count