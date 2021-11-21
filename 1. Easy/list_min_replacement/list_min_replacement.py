'''
Given a list of integers nums, replace every nums[i] with the smallest integer left of i. Replace nums[0] with 0.
'''

# Binary Search - Your code took 34 milliseconds — faster than 91.16% in Python

def list_min_replacement(nums):
    if nums:
        list_min = [0]
        holder = nums[0]
        for index in range(len(nums)-1):
            if nums[index] <= holder:
                holder = nums[index]
            list_min.append(holder)
        return list_min
    else:
        return []