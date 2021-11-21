
# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python

def high_five(n):
    string_n = str(n)
    if n > 0:
        for index, element in enumerate(string_n):
            if 5 > int(element):
                return int(string_n[:index] + "5" + string_n[index:])
        return int(string_n + "5")
    else:
        string_n = string_n.replace("-", "")
        for index, element in enumerate(string_n):
            if 5 < int(element):
                return int("-" + string_n[:index] + "5" + string_n[index:])
        return int("-" + string_n + "5")