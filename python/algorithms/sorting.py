from math import ceil
import random

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        index_min = i
        for j in range(i, len(arr)):
            if arr[index_min] > arr[j]: index_min = j
        if index_min != i: arr[index_min], arr[i] = arr[i], arr[index_min]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

def merge_sort(arr):
    if len(arr) <= 1: return arr
    middle = ceil(len(arr) / 2)
    left = arr[:middle]
    right = arr[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    merged = []
    while len(left) > 0 and len(right) > 0:
        if (left[0] < right[0]):
            merged.append(left[0])
            del left[0]
        else:
            merged.append(right[0])
            del right[0]

    merged += left + right
    return merged

# This is more readable, but uses more memory because it does not sort in-place
def quick_sort_simplified(arr):
    if len(arr) <= 1: return arr

    pivot = random.choice(arr)
    less_than = [val for val in arr if val < pivot]
    equal_to = [val for val in arr if val == pivot]
    greater_than = [val for val in arr if val > pivot]

    return quick_sort_simplified(less_than) + equal_to + quick_sort_simplified(greater_than)

def quick_sort_lomuto_partition(arr, low = 0, high = None):
    if high is None: high = len(arr) - 1
    if low < 0 or high < 0 or low >= high: return arr

    pivot_index = lomuto_partition(arr, low, high)
    # Because of this final swap in the partition, the pivot is excluded from the recursive call range here
    quick_sort_lomuto_partition(arr, low, pivot_index - 1)
    quick_sort_lomuto_partition(arr, pivot_index + 1, high)
    return arr

# Slower than Hoare partition, especially for inputs with a lot of duplicates
def lomuto_partition(arr, low, high):
    mid = (high - low) // 2 + low
    # Median-of-three pivot choice
    pivot = sorted([arr[0], arr[mid], arr[len(arr) - 1]])[1]
    # Must perform swaps to put the pivot at the end
    if arr[mid] < arr[low]: arr[low], arr[mid] = arr[mid], arr[low]
    if arr[high] < arr[low]: arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] < arr[high]: arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]
    pivot_index = low

    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1

    # Put the pivot into the correct location after the index has been found
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return pivot_index

def quick_sort_hoare_partition(arr, low = 0, high = None):
    if high is None: high = len(arr) - 1
    if len(arr) < 2 or low < 0 or high < 0 or low >= high: return arr

    pivot_index = hoare_partition(arr, low, high)
    quick_sort_hoare_partition(arr, low, pivot_index) # The pivot is now included
    quick_sort_hoare_partition(arr, pivot_index + 1, high)
    return arr

def hoare_partition(arr, low, high):
    # Rounded down so pivot can't be final position
    mid = (high - low) // 2 + low
    # Median-of-three pivot choice
    pivot = sorted([arr[0], arr[mid], arr[len(arr) - 1]])[1]
    left = low - 1
    right = high + 1

    while True:
        # This prevents the pointers from running off out of index without needing to test for it
        left += 1
        right -= 1
        while arr[left] < pivot: left += 1
        while arr[right] > pivot: right -= 1
        if left >= right: return right
        arr[left], arr[right] = arr[right], arr[left]
