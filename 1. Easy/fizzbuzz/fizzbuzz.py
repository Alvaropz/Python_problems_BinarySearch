'''
Given an integer n, return a list of integers from 1 to n as strings except for multiples of 3 use “Fizz” instead of the integer and for the multiples of 5 use “Buzz”. 

For integers which are multiples of both 3 and 5 use “FizzBuzz”.
'''

# Binary Search - Your code took 61 milliseconds — faster than 87.28% in Python.

def fizzbuzz(n):
    new_list = []
    for number in range(1, n+1):
        if number % 3 == 0 and number % 5 == 0:
            new_list.append("FizzBuzz")
        elif number % 3 == 0:
            new_list.append("Fizz")
        elif number % 5 == 0:
            new_list.append("Buzz")
        else:
            new_list.append(str(number))
    return new_list