'''
You are given a string animals and another string dinosaurs. 
Every letter in animals represents a different type of animal and every unique character in dinosaurs represents a different dinosaur.

Return the total number of dinosaurs in animals.
'''

# Binary Search - Your code took 13 milliseconds — faster than 100.00% in Python

def counting_dinosaurs(animals, dinosaurs):
    total_count = 0
    dinosaurs_list = list(set(dinosaurs))
    for dinosaur in dinosaurs_list:
        total_count += animals.count(dinosaur)
    return total_count