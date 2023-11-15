import pytest
from algorithms.sorting import *

@pytest.fixture
def pre_sorted():
    # Best case
    return [1, 2, 3, 4, 5, 6, 7]

@pytest.fixture
def reverse_sorted():
    # Worst case
    return [7, 6, 5, 4, 3, 2, 1]

@pytest.fixture
def random_unsorted():
    # Average case
    return [4, 2, 6, 1, 7, 3, 5]

@pytest.fixture
def unsorted_duplicates():
    # Edge case
    return [5, 1, 1, 2, 0, 0]

@pytest.fixture
def all_duplicates():
    # Edge case
    return [2, 2, 2, 2, 2, 2, 2]

def test_bubble_sort(pre_sorted, reverse_sorted, random_unsorted, unsorted_duplicates, all_duplicates):
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([2, 1]) == [1, 2]
    assert bubble_sort(pre_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert bubble_sort(reverse_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert bubble_sort(random_unsorted) == [1, 2, 3, 4, 5, 6, 7]
    assert bubble_sort(unsorted_duplicates) == [0, 0, 1, 1, 2, 5]
    assert bubble_sort(all_duplicates) == [2, 2, 2, 2, 2, 2, 2]

def test_selection_sort(pre_sorted, reverse_sorted, random_unsorted, unsorted_duplicates, all_duplicates):
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([2, 1]) == [1, 2]
    assert selection_sort(pre_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert selection_sort(reverse_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert selection_sort(random_unsorted) == [1, 2, 3, 4, 5, 6, 7]
    assert selection_sort(unsorted_duplicates) == [0, 0, 1, 1, 2, 5]
    assert selection_sort(all_duplicates) == [2, 2, 2, 2, 2, 2, 2]

def test_insertion_sort(pre_sorted, reverse_sorted, random_unsorted, unsorted_duplicates, all_duplicates):
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert insertion_sort([2, 1]) == [1, 2]
    assert insertion_sort(pre_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert insertion_sort(reverse_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert insertion_sort(random_unsorted) == [1, 2, 3, 4, 5, 6, 7]
    assert insertion_sort(unsorted_duplicates) == [0, 0, 1, 1, 2, 5]
    assert insertion_sort(all_duplicates) == [2, 2, 2, 2, 2, 2, 2]

def test_merge_sort(pre_sorted, reverse_sorted, random_unsorted, unsorted_duplicates, all_duplicates):
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([2, 1]) == [1, 2]
    assert merge_sort(pre_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert merge_sort(reverse_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert merge_sort(random_unsorted) == [1, 2, 3, 4, 5, 6, 7]
    assert merge_sort(unsorted_duplicates) == [0, 0, 1, 1, 2, 5]
    assert merge_sort(all_duplicates) == [2, 2, 2, 2, 2, 2, 2]

def test_merge_sort_in_place(pre_sorted, reverse_sorted, random_unsorted, unsorted_duplicates, all_duplicates):
    assert merge_sort_in_place([]) == []
    assert merge_sort_in_place([1]) == [1]
    assert merge_sort_in_place([2, 1]) == [1, 2]
    assert merge_sort_in_place(pre_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert merge_sort_in_place(reverse_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert merge_sort_in_place(random_unsorted) == [1, 2, 3, 4, 5, 6, 7]
    assert merge_sort_in_place(unsorted_duplicates) == [0, 0, 1, 1, 2, 5]
    assert merge_sort_in_place(all_duplicates) == [2, 2, 2, 2, 2, 2, 2]

def test_quick_sort_simplified(pre_sorted, reverse_sorted, random_unsorted, unsorted_duplicates, all_duplicates):
    assert quick_sort_simplified([]) == []
    assert quick_sort_simplified([1]) == [1]
    assert quick_sort_simplified([2, 1]) == [1, 2]
    assert quick_sort_simplified(pre_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_simplified(reverse_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_simplified(random_unsorted) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_simplified(unsorted_duplicates) == [0, 0, 1, 1, 2, 5]
    assert quick_sort_simplified(all_duplicates) == [2, 2, 2, 2, 2, 2, 2]

def test_quick_sort_lomuto_partition(pre_sorted, reverse_sorted, random_unsorted, unsorted_duplicates, all_duplicates):
    assert quick_sort_lomuto_partition([]) == []
    assert quick_sort_lomuto_partition([1]) == [1]
    assert quick_sort_lomuto_partition([2, 1]) == [1, 2]
    assert quick_sort_lomuto_partition(pre_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_lomuto_partition(reverse_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_lomuto_partition(random_unsorted) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_lomuto_partition(unsorted_duplicates) == [0, 0, 1, 1, 2, 5]
    assert quick_sort_lomuto_partition(all_duplicates) == [2, 2, 2, 2, 2, 2, 2]

def test_quick_sort_hoare_partition(pre_sorted, reverse_sorted, random_unsorted, unsorted_duplicates, all_duplicates):
    assert quick_sort_hoare_partition([]) == []
    assert quick_sort_hoare_partition([1]) == [1]
    assert quick_sort_hoare_partition([2, 1]) == [1, 2]
    assert quick_sort_hoare_partition(pre_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_hoare_partition(reverse_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_hoare_partition(random_unsorted) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_hoare_partition(unsorted_duplicates) == [0, 0, 1, 1, 2, 5]
    assert quick_sort_hoare_partition(all_duplicates) == [2, 2, 2, 2, 2, 2, 2]

def test_quick_sort_hoare_partition_alternative(pre_sorted, reverse_sorted, random_unsorted, unsorted_duplicates, all_duplicates):
    assert quick_sort_hoare_partition_alternative([]) == []
    assert quick_sort_hoare_partition_alternative([1]) == [1]
    assert quick_sort_hoare_partition_alternative([2, 1]) == [1, 2]
    assert quick_sort_hoare_partition_alternative(pre_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_hoare_partition_alternative(reverse_sorted) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_hoare_partition_alternative(random_unsorted) == [1, 2, 3, 4, 5, 6, 7]
    assert quick_sort_hoare_partition_alternative(unsorted_duplicates) == [0, 0, 1, 1, 2, 5]
    assert quick_sort_hoare_partition_alternative(all_duplicates) == [2, 2, 2, 2, 2, 2, 2]
