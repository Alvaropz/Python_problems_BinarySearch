'''
Given a non-negative integer n, return the length of the longest consecutive run of 1s in its binary representation.
'''

# Binary Search - Your code took 5 milliseconds — faster than 65.55% in Python.

def longest_consecutive_run_of_ones_in_binary(n):
    if n == 1:
        return 1
    bin_string = str(bin(n))[2:]
    i = 0
    j = len(bin_string)-1
    longest = 0
    while i+1 <= j:
        if bin_string[i] == "1":
            temp_value = 0
            while i+1 <= j  and bin_string[i] == "1":
                temp_value += 1
                i += 1
            if bin_string[i] == "1":
                temp_value += 1
            if temp_value > longest:
                longest = temp_value
        else:
            i += 1
    return longest