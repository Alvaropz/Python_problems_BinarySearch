'''
The Fibonacci sequence goes like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number can be found by adding up the two numbers before it, and the first two numbers are always 1.

Write a function that takes an integer n and returns the nth Fibonacci number in the sequence.

Note: n will be less than or equal to 30.
'''

#Binary Search - Your code took 1 millisecond — faster than 100.00% in Python

def fibonacci( n):
    list_fibo = [1, 1]
    count = 2
    while count < n :
        list_fibo.append(list_fibo[-2] + list_fibo[-1])
        count += 1
    return list_fibo[-1]
            