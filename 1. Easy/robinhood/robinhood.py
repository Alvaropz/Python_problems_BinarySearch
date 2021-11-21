'''
You are given integers n, e, o, t. You have n dollars in principal that you invested in the stock market. 

Given the stock market alternates between first returning e and then o percent interest per year, return how many years it would take to reach at leastt dollars.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def robinhood(n, e, o, t):
    if n < t:
        years = 0
        while n < t:
            years += 1
            if years % 2 == 0:
                n += (n * (o / 100))
            else:
                n += (n * (e / 100))
        return years
    return 0