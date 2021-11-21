'''
You are given a list of strings orders. Each element in orders starts with either "P" meaning pickup or "D" meaning delivery followed by the order id. For example, "P12" means pick up order 12.

Return whether orders is valid given the following rules:

A delivery cannot happen for an order before pickup
Every pickup must be delivered
An order that's already been picked up and delivered cannot be picked up or delivered again
'''

# Binary Search - Your code took 63 milliseconds — faster than 72.98% in Python.

def validate_delivery_orders(orders):
    d = {}
    total_pic = 0
    total_del = 0
    for deliv in orders:
        status = deliv[0]
        orderN = deliv[1:]
        if status == "P" and not deliv in d:
            d[deliv] = 0
            total_pic += 1
        elif status == "P" and deliv in d:
            return False
        elif status == "D" and "P" + orderN in d and d["P"+orderN] == 0:
            d["P"+orderN] = 1
            total_del += 1
        else:
            return False
    if total_del != total_pic:
        return False
    return True