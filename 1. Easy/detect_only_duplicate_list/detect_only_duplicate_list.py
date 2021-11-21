'''
You are given a list nums of length n + 1 picked from the range 1, 2, ..., n. By the pigeonhole principle, there must be a duplicate. 
Find and return it. There is guaranteed to be exactly one duplicate.

Bonus: Can you do this in \mathcal{O}(n)O(n) time and \mathcal{O}(1)O(1) space?
'''

#Binary Search - Your code took 31 milliseconds — faster than 54.16% in Python

from collections import Counter

def only_duplicate(nums):
    count_dict = Counter(nums)
    for key, value in count_dict.items():
        if value > 1:
            return key