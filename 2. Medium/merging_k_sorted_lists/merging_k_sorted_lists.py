'''
Given a list of sorted lists of integers, merge them into one large sorted list.
'''

# Binary Search - Your code took 73 milliseconds — faster than 24.08% in Python.

def merging_k_sorted_lists(lists):
    return sorted([item for sublist in lists for item in sublist])

# Binary Search - Your code took 432 milliseconds — faster than 12.04% in Python.

from heapq import heappush, heappop

def merging_k_sorted_lists_right_way(lists):
    minHeap = []
    for row, l in enumerate(lists):
        if l:
            heappush(minHeap, (l[0], row, 0))

    result = []
    while minHeap:
        item, row, col = heappop(minHeap)
        result.append(item)

        # Add the next element from this list
        if col < len(lists[row]) - 1:
            heappush(minHeap, (lists[row][col + 1], row, col + 1))

    return result