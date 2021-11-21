'''
You are given a list of lists fractions where each list contains [numerator, denominator] which represents the number numerator / denominator.

Return a new list of lists such that the numbers in fractions are:

In their most reduced terms. E.g. 8 / 6 becomes 4 / 3.
Any duplicate fractions that represent the same value are removed.
Sorted in ascending order by their value.
If the number is negative, the - sign should go to the numerator (the input also follows this).
'''

# Binary Search - Your code took 112 milliseconds — faster than 48.22% in Python.

import math

def unique_fractions(fractions):
    min_list = []
    for fraction in fractions:
        min_gcd = math.gcd(fraction[0], fraction[1])
        min_list.append([int(fraction[0]/min_gcd), int(fraction[1]/min_gcd)])
    remove_duplicates_set = set()
    list_of_tuples = []
    for fraction in min_list:
        if not (fraction[0]/fraction[1]) in remove_duplicates_set:
            remove_duplicates_set.add(fraction[0]/fraction[1])
            list_of_tuples.append((fraction[0]/fraction[1], fraction))
    list_of_tuples.sort()
    return [sub_list[1] for sub_list in list_of_tuples]