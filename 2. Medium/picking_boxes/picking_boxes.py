'''
Given a list of integers nums, pack consecutive elements of the same value into sublists.

Note: If there's only one occurrence in the list it should still be in its own sublist.
'''

# Binary Search - Your code took 52 milliseconds — faster than 26.88% in Python.

def picking_boxes(nums):
    if nums:
        boxes = [[nums[0]]]
        i = 1
        j = len(nums)-1    
        while i <= j:
            if nums[i] in boxes[-1]:
                boxes[-1].append(nums[i])
            else:
                boxes.append([nums[i]])
            i += 1
        return boxes
    return []