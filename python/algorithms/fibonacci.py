# Note that with recursive solutions using memoization, it can't be as memory
# efficient as bottom-up because we need to store the entire collection of
# numbers as we work from the top down - otherwise we will be overwriting the calculation with different recursive calls using a pass-by-reference data type.
def fibonacci_memo_list(n: int, memo: list = None):
    if n < 2: return n
    if memo is None: memo = [None] * (n + 1)
    if memo[n] is not None: return memo[n]
    memo[n] = fibonacci_memo_list(n - 1, memo) + fibonacci_memo_list(n - 2, memo)

    return memo[n]

def fibonacci_memo_dict(n: int, memo: dict = {0: 0, 1: 1, 2: 1}):
    if n in memo: return memo[n]
    memo[n] = fibonacci_memo_dict(n - 1, memo) + fibonacci_memo_dict(n - 2, memo)
    # Memory optimization
    if n > 2: del memo[n - 3]

    return memo[n]

def fibonacci():
    memo = {0: 0, 1: 1, 2: 1}
    def fibonacci_with_closure(n: int):
        nonlocal memo
        if n in memo: return memo[n]
        memo[n] = fibonacci_with_closure(n - 1) + fibonacci_with_closure(n - 2)
        # Memory optimization
        del memo[n - 3]
        return memo[n]

    return fibonacci_with_closure

# Bottom-up is more memory efficient because we only need to save the
# accumulator as we calculate it from the bottom up.
def fibonacci_bottom_up_tabulation(n: int):
    if n < 2: return n
    nums = [0, 1]

    for i in range(2, n + 1):
        nums += [nums[i - 1] + nums[i - 2]]

    return nums[n]

def fibonacci_bottom_up_space_optimized(n: int):
    if n < 2: return n
    prev1 = 1
    prev2 = 0
    # Note that iterating over a range uses a generator instead of a list
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1

def fibonacci_generator(n: int):
    prev2 = 0
    prev1 = 1
    yield 0
    yield 1
    for _ in range(n - 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
        yield prev1
