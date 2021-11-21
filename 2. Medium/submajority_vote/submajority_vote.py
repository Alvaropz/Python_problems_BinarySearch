'''
You are given a list of integers nums where each number represents a vote to a candidate.

Return the ids of the candidates that have greater than |n/3| votes, in ascending order.

Bonus: solve in \mathcal{O}(1)O(1) space.
'''

# Binary Search - Your code took 60 milliseconds — faster than 71.86% in Python.

from collections import Counter

def submajority_vote(nums):
    min_votes = len(nums)/3
    dict_votes = Counter(nums)
    for key in dict_votes:
        dict_votes[key] = dict_votes[key]
    return sorted([key for key, value in dict_votes.items() if value > min_votes])