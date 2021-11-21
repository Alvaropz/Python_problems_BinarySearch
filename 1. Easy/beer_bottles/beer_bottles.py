'''
You are given an integer n representing n full beer bottles. 

Given that you can exchange 3 empty beer bottles for 1 full beer bottle, return the number of beer bottles you can drink.
'''

# Binary Search - Your code took 16 milliseconds — faster than 7.69% in Python.

def beer_bottles(n):
    total = n
    holding_beers = 0
    while n > 0:
        if n % 3 == 0:
            total += int(n/3)
            n = int(n/3)
            n += holding_beers
            holding_beers = 0
        else:
            holding_beers += 1
            n -= 1
    return total