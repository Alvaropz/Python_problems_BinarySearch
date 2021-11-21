'''
Given two lists of integers a and b, as well as an integer k, return the number of elements in a that are strictly smaller than at least k elements in b.
'''

# Binary Search - Your code took 35 milliseconds — faster than 96.93% in Python

def k_compare(a, b, k):
    if k == 0:
        return len(a)
    greatest_n = sorted(b)[-k]
    total = 0
    for number in a:
        if number < greatest_n:
            total += 1
    return total