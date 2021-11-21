'''
Given a two dimensional list of integers votes, where each list has two elements [candidate_id, voter_id], report whether any voter has voted more than once.
'''

# Binary Search - Your code took 9 milliseconds — faster than 30.60% in Python

from collections import Counter

def detect_voter_fraud(votes):
    voters_id = []
    for pair in votes:
        voters_id.append(pair[1])
    dict_counting = Counter(voters_id)
    for number_votes in dict_counting.values():
        if number_votes > 1:
            return True
    return False