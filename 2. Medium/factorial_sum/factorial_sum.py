'''
Given a positive integer n, return whether n can be written as the sum of distinct positive factorial numbers.
Input: 31
Output: True

Since 31 = 4! + 3! + 1!
'''

# Binary Search - Your code took 11 milliseconds — faster than 23.62% in Python.

def factorial_sum(n):
    number_list = []
    for number in range(1, n+1):
        temp_factor = number
        for factor in range(1, number):
            temp_factor = temp_factor * (number - factor)
        if temp_factor > n:
            break
        number_list.append(temp_factor)
    for number in number_list[::-1]:
        if n - number >= 0:
            n -= number
        if n == 0:
            return True
    return False