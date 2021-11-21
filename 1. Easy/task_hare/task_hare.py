'''
You are given a list of integers tasks and another list of integers people. The integer tasks[i] represents the amount of strength required to perform the ith task. people[i] represents the amount of strength the ith person has.

Return the number of tasks that can be finished if one person can perform at most one task.
'''

# Binary Search - Your code took 470ms in python — faster than 73.68% in Python.

def task_hare(tasks, people):
    tasks.sort()
    people.sort()
    finished_tasks = 0
    i_people = 0
    i_tasks = 0
    j_people = len(people)-1
    j_tasks = len(tasks)-1
    while i_people <= j_people and i_tasks <= j_tasks:
        if people[i_people] >= tasks[i_tasks]:
            finished_tasks += 1
            i_tasks += 1
        i_people += 1
    return finished_tasks