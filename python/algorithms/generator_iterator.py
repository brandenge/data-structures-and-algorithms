# Generator function
def my_generator_num(n: int):
    for i in range(1, n + 1):
        yield i

# Iterator function
def my_iterator(iterable: int, func):
    iterator = iter(iterable)
    res = []
    while True:
        try: res.append(func(next(iterator)))
        except StopIteration: break
    return res

class MyIterator():
    # Iterator class has 2 pointers or values
    def __init__(self, first, last):
        self.curr = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        # condition always compares the 2 pointers/values
        # to determine when to raise the StopIteration error
        if self.curr <= self.last:
            curr = self.curr
            self.curr += 1
            # Returns the current value
            return curr
        raise StopIteration
