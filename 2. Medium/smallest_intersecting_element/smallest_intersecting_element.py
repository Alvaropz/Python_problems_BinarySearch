'''
You are given a two-dimensional list of integers matrix where each row is sorted in ascending order. 

Return the smallest number that exists in every row. If there's no solution, return -1.
'''

# Binary Search - Your code took 29 milliseconds — faster than 97.27% in Python.

def smallest_intersecting_element(matrix):
    if not matrix:
        return -1
    list_numbers = []
    for number in matrix[0]:
        temp = number
        for i in range(1, len(matrix)):
            if not number in matrix[i]:
                temp = -1
                break
        if temp != -1:
            list_numbers.append(temp)
    if list_numbers:
        return min(list_numbers)
    else:
        return -1