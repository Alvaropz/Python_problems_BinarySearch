'''
You are given a two-dimensional list of integers relations. Each element relations[i] contains [a, b] meaning that person a is following person b on Twitter.

Return the list of people who follow someone that follows them back, sorted in ascending order.
'''

# Binary Search - Your code took 149 milliseconds — faster than 81.63% in Python.

from collections import Counter

def mutual_followers(relations):
    for i, relation in enumerate(relations):
        if relations[i][0] > relations[i][1]:
            relations[i] = tuple(sorted(relation))
        else:
            relations[i] = tuple(relation)
    returned_list = []
    dict_counting = Counter(relations)
    for key in dict_counting:
        if dict_counting[key] >= 2:
            returned_list.extend(key)
    return sorted(set(returned_list))