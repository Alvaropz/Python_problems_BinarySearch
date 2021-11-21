'''
Given an integer n, return the nth (0-indexed) row of Pascal's triangle.

Pascal's triangle can be created as follows: In the top row, there is an array of 1. Each subsequent row is created by adding the number above and to the left with the number above and to the right, treating empty elements as 0.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python

def pascals_triangle(n):
    pascal = [[1]]
    for i in range(1, n+1):
        temp_pascal = [1]
        for i in range(1, len(pascal[-1])):
            temp_pascal.append(pascal[-1][i] + pascal[-1][i-1])
        temp_pascal.append(1)
        pascal.append(temp_pascal)
    return pascal[-1]