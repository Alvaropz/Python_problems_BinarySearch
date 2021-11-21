'''
You are given n people represented as an integer from 0 to n - 1, and a list of friends tuples, where person friends[i][0] and person friends[i][1] are friends.

Return whether everyone has at least one friend.
'''

# Binary Search - Your code took 4 milliseconds — faster than 45.05% in Python.

def no_new_friends(n, friends):
    dict_friends = {}
    for sub_list in friends:
        for friend_number in sub_list:
            if friend_number in dict_friends:
                dict_friends[friend_number] += 1
            else:
                dict_friends[friend_number] = 1
    list_uniques = list(dict_friends.fromkeys(dict_friends))
    return len(list_uniques) == n
