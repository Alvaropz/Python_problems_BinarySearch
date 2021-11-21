'''
Given a list of integers prices representing the stock prices of a company in chronological order, return the maximum profit you could have made from buying and selling that stock any number of times.

You must buy before you can sell it. But you are not required to buy or sell the stock.
'''

# Binary Serach - Your code took 95 milliseconds — faster than 10.47% in Python.

def wolves_of_wall_street(prices):
    i = 0
    j = len(prices)-1
    total_profit = 0
    while i < j:
        if prices[i] <= prices[i+1]:
            curr_min_value = prices[i]
            curr_max_profit = prices[i+1]
            i += 1
            while curr_max_profit <= prices[i]:
                curr_max_profit = prices[i]
                if i == len(prices)-1:
                    break
                i += 1
            total_profit += (curr_max_profit - curr_min_value)
        else:
            i += 1
    return total_profit