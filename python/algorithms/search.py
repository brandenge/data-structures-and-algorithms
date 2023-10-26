def linear_search_iterative(value, array):
    for i in range(len(array)):
        if array[i] == value: return i

def linear_search_recursive(value, array, i = 0):
    if i >= len(array): return None
    if array[i] == value: return i
    return linear_search_recursive(value, array, i + 1)

def binary_search_iterative(value, array):
    left = 0
    right = len(array) - 1
    middle = (left + right) // 2
    while left <= right:
        if array[middle] == value: return middle
        elif array[middle] < value: left = middle + 1
        elif array[middle] > value: right = middle - 1
        middle = (left + right) // 2

def binary_search_recursive(value, array, left = None, right = None):
    if left is None and right is None:
        left = 0
        right = len(array) - 1
    middle = (left + right) // 2
    if left > right: return None
    if array[middle] == value: return middle
    if array[middle] < value: left = middle + 1
    elif array[middle] > value: right = middle - 1
    return binary_search_recursive(value, array, left, right)
