'''
You are given a list of integers fighters and a two dimensional list bosses. The fighters list contains 1s and 0s with a 1 representing a fighter. Similarly, each bosses list contains 1s and 0s with a 1 representing a boss.

Given that fighters can beat a bosses row if it contains more fighters than bosses, return a new bosses matrix with defeated boss rows removed.
'''

from collections import Counter

# Binary Search - Your code took 222 milliseconds — faster than 7.48% in Python

def boss_fight(fighters, bosses):
    fighters_count = Counter(fighters)
    new_boss_list = []
    for current_boss_list in bosses:
        temp_boss = Counter(current_boss_list)
        if temp_boss[1] >= fighters_count[1]:
            new_boss_list.append(current_boss_list)
    return new_boss_list
