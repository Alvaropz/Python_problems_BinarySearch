'''
Given a list of strings shows, a list of integers durations, and an integer k, where shows[i] and durations[i] represent the name and duration watched by the ith person, return the total duration watched of the k most watched shows.
'''

# Binary Search - Your code took 28 milliseconds — faster than 97.37% in Python.

def k_longest_show_durations(shows, durations, k):
    d = {}
    for i, show in enumerate(shows):
        if show in d:
            d[show] += durations[i]
        else:
            d[show] = durations[i]
    return sum(list(reversed(sorted(d.values())))[:k])