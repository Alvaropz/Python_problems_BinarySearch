'''
You are given a string s of "a" and "b"s. "a"s can stay "a" or turn into "b", but "b"s can't change.

Return the number of unique strings that can be made.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def unique_ab_string(s):
    n_a = s.count("a")
    total = 0
    for number in range(1, n_a):
        total += (total + number)
    return total + n_a + 1