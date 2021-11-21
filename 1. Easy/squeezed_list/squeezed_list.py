'''
Given a list of integers nums, squeeze from both the left and the right of nums until there is one remaining element. Return the states at each step.
'''

# Binary Search - Your code took 8 milliseconds — faster than 22.34% in Python

def squeezed_list(nums):
    matrix = [nums.copy()]
    while len(matrix[-1]) > 1:
        if len(matrix[-1]) > 4:
            temp_list = []
            temp_list.append(matrix[-1][0]+matrix[-1][1])
            temp_list.extend(matrix[-1][2:-2])
            temp_list.append(matrix[-1][-2]+matrix[-1][-1])
            matrix.append(temp_list)
        if len(matrix[-1]) == 4:
            temp_list = []
            temp_list.append(matrix[-1][0]+matrix[-1][1])
            temp_list.append(matrix[-1][-2]+matrix[-1][-1])
            matrix.append(temp_list)
        if len(matrix[-1]) == 3:
            temp_list = []
            temp_list.append(sum(matrix[-1]))
            matrix.append(temp_list)
        if len(matrix[-1]) == 2:
            temp_list = []
            temp_list.append(matrix[-1][0]+matrix[-1][1])
            matrix.append(temp_list)
    return matrix

# Binary Search - Your code took 4 milliseconds — faster than 97.80% in Python (Code provided by inmortal)

def squeezed_list_optimised(nums):
    left, right = 0, len(nums)
    ans = []
    while left < right:
        ans.append(nums[left:right])
        left += 1
        right -= 1
        nums[left] += nums[left - 1]
        nums[right - 1] += nums[right]

    if len(nums) % 2 == 0:
        ans.append(nums[left : right + 1])
    return ans