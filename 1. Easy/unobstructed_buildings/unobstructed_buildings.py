'''
You are given a list of integers heights representing building heights. A building heights[i] can see the ocean if every building on its right has shorter height. 

Return the building indices where you can see the ocean, in ascending order.
'''

# Binary Search - Your code took 13 milliseconds — faster than 100.00% in Python.

def unobstructed_buildings(heights):
    if heights:
        index_list = []
        max_height = heights[-1]
        for index, high in enumerate(reversed(heights)):
            if high > max_height:
                index_list.append(len(heights)-index-1)
                max_height = high
        index_list.append(len(heights)-1)
        return sorted(index_list)
    return []
