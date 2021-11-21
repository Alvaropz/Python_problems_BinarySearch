'''
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
'''

# Binary Search - Your code took 3 milliseconds — faster than 100.00% in Python.

def making_change_v_one(n):
    count = 0
    count += n//25
    n = n%25
    count += n//10
    n = n%10
    count += n//5
    n = n%5
    count += n//1
    n = n%1
    return count

# Binary Search - Your code took 3 milliseconds — faster than 100.00% in Python.

def making_change_v_two(n):
    total = 0
    if n // 25 >= 0:
        total += (n//25)
        n = n%25
    if n // 10 >= 0:
        total += (n//10)
        n = n%10
    if n // 5 >= 0:
        total += (n//5)
        n = n%5
    return total + n