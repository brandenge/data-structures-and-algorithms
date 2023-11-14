from algorithms.generator_iterator import *

def test_generator_num():
    gen = my_generator_num(5)
    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 4
    assert next(gen) == 5

def test_my_iterator():
    iterable = [1, 2, 3, 4, 5]
    assert my_iterator(iterable, lambda n: n * 2) == [2, 4, 6, 8, 10]

def test_iterator_class():
    my_gen = MyIterator(1, 5)
    assert next(my_gen) == 1
    assert next(my_gen) == 2
    assert next(my_gen) == 3
    assert next(my_gen) == 4
    assert next(my_gen) == 5
