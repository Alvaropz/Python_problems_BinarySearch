'''
You are given a list of integers nums, representing a decimal number and nums[i] is between [0, 9].

For example, [1, 3, 9] represents the number 139.

Return the same list in the same representation except modified so that 1 is added to the number.
'''

#Binary Search - Your code took 67 milliseconds — faster than 75.81% in Python

def add_one(nums):
    nums.reverse()
    nums[0] += 1
    for index, number in enumerate(nums):
        if number == 10:
            nums[index] = 0
            if index+1 < len(nums):
                nums[index+1] += 1
            elif index+1 == len(nums):
                nums.insert(index+1, 1)
    nums.reverse()
    return nums