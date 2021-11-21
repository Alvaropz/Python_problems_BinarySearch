'''
Given a list of integers prices representing the stock prices of a company in chronological order, return the maximum profit you could have made from buying and selling that stock once.

You must buy before you can sell it.

Note: You are not required to buy or sell the stock.
'''

# Binary Search - Your code took 24 milliseconds — faster than 98.54% in Python.

def wolf_of_wall_street(prices):
    if prices:
        max_price = 0
        difference = 0
        for price in prices[::-1]:
            if max_price < price:
                max_price = price
            if max_price - price > difference:
                difference = max_price - price
        return difference
    return 0

# Binary Search - Your code took 122 milliseconds — faster than 67.20% in Python.

def wolf_of_wall_street_less_optimed(prices):
    if prices:
        min_price = (0, max(prices))
        max_price = (0, 0)
        list_result = []
        for idx, num in enumerate(prices):
            if idx >= min_price[0] and num < min_price[1]:
                min_price = (idx, num)
            if idx >= max_price[0] and num > min_price[1]:
                max_price = (idx, num)
            if min_price[0] < max_price[0] and max_price[1] - min_price [1] >= 0:
                list_result.append(max_price[1] - min_price [1])
        if list_result:
            return max(list_result)
    return 0