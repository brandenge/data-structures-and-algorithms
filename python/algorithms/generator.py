def my_generator_num(n: int):
    for i in range(1, n + 1):
        yield i

def my_generator_iterable(iterable: int, func):
    iterator = iter(iterable)
    res = []
    while True:
        try:
            res.append(func(next(iterator)))
        except StopIteration:
            break
    return res

class MyGenerator():
    def __init__(self, first, last):
        self.curr = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr <= self.last:
            curr = self.curr
            self.curr += 1
            return curr
        raise StopIteration
