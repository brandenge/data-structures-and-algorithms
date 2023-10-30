from algorithms.fibonacci import *

def test_fibonacci_memo_list():
    assert fibonacci_memo_list(0) == 0
    assert fibonacci_memo_list(1) == 1
    assert fibonacci_memo_list(2) == 1
    assert fibonacci_memo_list(3) == 2
    assert fibonacci_memo_list(4) == 3
    assert fibonacci_memo_list(5) == 5
    assert fibonacci_memo_list(6) == 8
    assert fibonacci_memo_list(10) == 55
    assert fibonacci_memo_list(20) == 6765
    assert fibonacci_memo_list(30) == 832040
    assert fibonacci_memo_list(40) == 102334155
    assert fibonacci_memo_list(50) == 12586269025

def test_fibonacci_memo_dict():
    assert fibonacci_memo_dict(0) == 0
    assert fibonacci_memo_dict(1) == 1
    assert fibonacci_memo_dict(2) == 1
    assert fibonacci_memo_dict(3) == 2
    assert fibonacci_memo_dict(4) == 3
    assert fibonacci_memo_dict(5) == 5
    assert fibonacci_memo_dict(6) == 8
    assert fibonacci_memo_dict(10) == 55
    assert fibonacci_memo_dict(20) == 6765
    assert fibonacci_memo_dict(30) == 832040
    assert fibonacci_memo_dict(40) == 102334155
    assert fibonacci_memo_dict(50) == 12586269025

def test_fibonacci_memo_closure():
    fibonacci_with_closure = fibonacci()
    assert fibonacci_with_closure(0) == 0
    assert fibonacci_with_closure(1) == 1
    assert fibonacci_with_closure(2) == 1
    assert fibonacci_with_closure(3) == 2
    assert fibonacci_with_closure(4) == 3
    assert fibonacci_with_closure(5) == 5
    assert fibonacci_with_closure(6) == 8
    assert fibonacci_with_closure(10) == 55
    assert fibonacci_with_closure(20) == 6765
    assert fibonacci_with_closure(30) == 832040
    assert fibonacci_with_closure(40) == 102334155
    assert fibonacci_with_closure(50) == 12586269025

def test_fibonacci_bottom_up_tabulation():
    assert fibonacci_bottom_up_tabulation(0) == 0
    assert fibonacci_bottom_up_tabulation(1) == 1
    assert fibonacci_bottom_up_tabulation(2) == 1
    assert fibonacci_bottom_up_tabulation(3) == 2
    assert fibonacci_bottom_up_tabulation(4) == 3
    assert fibonacci_bottom_up_tabulation(5) == 5
    assert fibonacci_bottom_up_tabulation(6) == 8
    assert fibonacci_bottom_up_tabulation(10) == 55
    assert fibonacci_bottom_up_tabulation(20) == 6765
    assert fibonacci_bottom_up_tabulation(30) == 832040
    assert fibonacci_bottom_up_tabulation(40) == 102334155
    assert fibonacci_bottom_up_tabulation(50) == 12586269025

def test_fibonacci_bottom_up_space_optimized():
    assert fibonacci_bottom_up_space_optimized(0) == 0
    assert fibonacci_bottom_up_space_optimized(1) == 1
    assert fibonacci_bottom_up_space_optimized(2) == 1
    assert fibonacci_bottom_up_space_optimized(3) == 2
    assert fibonacci_bottom_up_space_optimized(4) == 3
    assert fibonacci_bottom_up_space_optimized(5) == 5
    assert fibonacci_bottom_up_space_optimized(6) == 8
    assert fibonacci_bottom_up_space_optimized(10) == 55
    assert fibonacci_bottom_up_space_optimized(20) == 6765
    assert fibonacci_bottom_up_space_optimized(30) == 832040
    assert fibonacci_bottom_up_space_optimized(40) == 102334155
    assert fibonacci_bottom_up_space_optimized(50) == 12586269025

def test_fibonacci_generator():
    fib_nums = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
    fib_gen = fibonacci_generator(20)
    for i, n in enumerate(fib_gen):
        assert fib_nums[i] == n
