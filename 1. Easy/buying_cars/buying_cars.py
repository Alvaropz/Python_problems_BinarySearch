'''
Given a list of integers prices representing prices of cars for sale, and a budget k, return the maximum number of cars you can buy.
'''

# Binary Search - Your code took 11 milliseconds — faster than 99.11% in Python


def buying_cars(prices, k):
    prices.sort()
    count = 0
    for price in prices:
        if k >= price:
            count += 1
            k -= price
    return count