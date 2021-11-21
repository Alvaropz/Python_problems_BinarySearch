'''
Given lowercase alphabet strings s0, s1 and a positive integer n, return the nth term of the sequence A where:

A[0] = s0
A[1] = s1
A[n] = A[n - 1] + A[n - 2] if n is even, otherwise A[n] = A[n - 2] + A[n - 1].
'''

# Binary Search - Your code took 2 milliseconds — faster than 91.18% in Python.

def string_sequence(s0, s1, n):
    list_strings = [s0, s1]
    i = 2
    while i <= n:
        if i % 2 == 0:
            list_strings.append(list_strings[i-1] + list_strings[i-2])
        else:
            list_strings.append(list_strings[i-2] + list_strings[i-1])
        i += 1
    return list_strings[n]