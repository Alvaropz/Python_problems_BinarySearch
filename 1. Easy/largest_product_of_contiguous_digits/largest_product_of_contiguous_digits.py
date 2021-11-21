'''
Given two integers num and k, return the largest product of k contiguous digits in num.

Note: num is guaranteed to have >= k digits.
'''

# Binary Search - Your code took 1 millisecond — faster than 99.37% in Python.

def largest_product_of_contiguous_digits(num, k):
    string_num = [str(number) for number in str(num)]
    k_list = []
    for idx, n in enumerate(string_num):
        lenght = k-1
        idx_ref = idx+1
        temp_list = [n]
        if idx_ref + lenght <= len(string_num):
            while lenght > 0:
                temp_list.append(string_num[idx_ref])
                idx_ref += 1
                lenght -= 1
        else:
            break
        k_list.append(temp_list)
    product_list = []
    for sub_list in k_list:
        i = 0
        j = len(sub_list)-1
        product = 1
        while i <= j:
            product *= int(sub_list[i])
            i += 1
        product_list.append(product)
    return max(product_list)