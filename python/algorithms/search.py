def linear_search_iterative(value, arr):
    for i in range(len(arr)):
        if arr[i] == value: return i

def linear_search_recursive(value, arr, i = 0):
    if i >= len(arr): return None
    if arr[i] == value: return i
    return linear_search_recursive(value, arr, i + 1)

def binary_search_iterative(value, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == value: return mid
        elif arr[mid] < value: left = mid + 1
        elif arr[mid] > value: right = mid - 1

def binary_search_recursive(value, arr, left = None, right = None):
    if left is None and right is None:
        left = 0
        right = len(arr) - 1
    mid = (left + right) // 2
    if left > right: return None
    if arr[mid] == value: return mid
    if arr[mid] < value: left = mid + 1
    elif arr[mid] > value: right = mid - 1
    return binary_search_recursive(value, arr, left, right)
