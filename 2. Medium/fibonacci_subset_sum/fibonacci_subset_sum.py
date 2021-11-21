'''
Given an integer n, return the minimum number of Fibonacci numbers required to sum up to n.
'''

# Binary Search - Your code took 38 milliseconds — faster than 78.38% in Python.

def fibonacci_subset_sum(n):
    fibo = [1, 1]
    for number in range(n):
        sum_fibo = fibo[-1] + fibo[-2]
        if sum_fibo > n:
            break
        fibo.append(sum_fibo)
    c_sum = 0
    total = 0
    for number in fibo[::-1]:
        if c_sum + number < n:
            c_sum += number
            total += 1
        if c_sum + number == n:
            return total + 1