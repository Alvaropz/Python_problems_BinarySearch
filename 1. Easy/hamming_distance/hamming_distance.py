'''
Given two integers x, and y return the number of positions where their values differ in their binary representations as a 32-bit integer.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python

def hamming_distance(x, y):
    count = 0
    bin_x = '{:032b}'.format(x)
    bin_y = '{:032b}'.format(y)
    for x_val, y_val in zip(bin_x, bin_y):
        if x_val != y_val:
            count += 1
    return count