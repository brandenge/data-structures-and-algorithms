from algorithms.search import *

def test_linear_search_iterative():
    array = [7, 6, 5, 4, 3, 2, 1]
    assert linear_search_iterative(0, array) == None
    assert linear_search_iterative(1, array) == 6
    assert linear_search_iterative(2, array) == 5
    assert linear_search_iterative(3, array) == 4
    assert linear_search_iterative(4, array) == 3
    assert linear_search_iterative(5, array) == 2
    assert linear_search_iterative(6, array) == 1
    assert linear_search_iterative(7, array) == 0
    assert linear_search_iterative(8, array) == None
    assert linear_search_iterative(1, []) == None

def test_linear_search_recursive():
    array = [7, 6, 5, 4, 3, 2, 1]
    assert linear_search_recursive(0, array) == None
    assert linear_search_recursive(1, array) == 6
    assert linear_search_recursive(2, array) == 5
    assert linear_search_recursive(3, array) == 4
    assert linear_search_recursive(4, array) == 3
    assert linear_search_recursive(5, array) == 2
    assert linear_search_recursive(6, array) == 1
    assert linear_search_recursive(7, array) == 0
    assert linear_search_recursive(8, array) == None
    assert linear_search_recursive(1, []) == None

def test_binary_search_iterative():
    array = [1, 2, 3, 4, 5, 6, 7]
    assert binary_search_iterative(0, array) == None
    assert binary_search_iterative(1, array) == 0
    assert binary_search_iterative(2, array) == 1
    assert binary_search_iterative(3, array) == 2
    assert binary_search_iterative(4, array) == 3
    assert binary_search_iterative(5, array) == 4
    assert binary_search_iterative(6, array) == 5
    assert binary_search_iterative(7, array) == 6
    assert binary_search_iterative(8, array) == None
    assert binary_search_iterative(1, []) == None

def test_binary_search_recursive():
    array = [1, 2, 3, 4, 5, 6, 7]
    assert binary_search_recursive(0, array) == None
    assert binary_search_recursive(1, array) == 0
    assert binary_search_recursive(2, array) == 1
    assert binary_search_recursive(3, array) == 2
    assert binary_search_recursive(4, array) == 3
    assert binary_search_recursive(5, array) == 4
    assert binary_search_recursive(6, array) == 5
    assert binary_search_recursive(7, array) == 6
    assert binary_search_recursive(8, array) == None
    assert binary_search_recursive(1, []) == None
