'''
You are given a list of integers nums and integers k and target. Consider an operation where we choose an integer -k ≤ e ≤ k and append it to nums.

Return the minimum number of operations required such that the sum of nums equals to target.
'''

# Binary Search - Your code took 21 milliseconds — faster than 1.04% in Python.

def append_list_to_sum_target(nums, k, target):
    total_sum = sum(nums)
    count = 0
    if target > total_sum:
        while total_sum != target:
            if total_sum + k <= target:
                nums.append(k)
                count +=1
            if total_sum + k > target:
                k -= 1
            total_sum = sum(nums)
    elif target < total_sum:
        k *= -1
        while total_sum != target:
            if total_sum + k >= target:
                nums.append(k)
                count +=1
            if total_sum + k < target:
                k += 1
            total_sum = sum(nums)
    return count

# Binary Search - Your code took 4 milliseconds — faster than 41.67% in Python.

def append_list_to_sum_target_optimised(nums, k, target):
    total_sum = sum(nums)
    count = 0
    while total_sum != target:
        if target > total_sum:
            if total_sum + k <= target and k > 0:
                total_sum += k
                count += 1
            if total_sum + k > target and k > 0:
                k -= 1
        if total_sum > target:
            if k > 0:
                k *= -1
            if total_sum + k >= target and not total_sum + k < target:
                total_sum += k
                count += 1
            elif total_sum + k < target:
                k += 1
    return count