'''
You are given a list of integers nums, representing the number of chess matches each person has won. Return a relative ranking (0-indexed) of each person. 

If two players have won the same amount, their ranking should be the same.
'''

# Binary Search - Your code took 402 milliseconds — faster than 26.83% in Python.

def leaderboard(nums):
    list_uniques = list(sorted(list(dict.fromkeys(nums))))[::-1]
    dict_position = {}
    for idx, number in enumerate(list_uniques):
        dict_position[number] = idx
    for idx, number in enumerate(nums):
        nums[idx] = dict_position[number]
    return nums