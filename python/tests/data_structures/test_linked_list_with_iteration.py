import pytest
from data_structures.linked_list_with_iteration import LinkedListWithIteration as List
from fixtures.linked_lists_with_iteration import list, small_list

def test_initialization(list):
    assert list.is_empty()
    assert list.count() == 0

def test_is_empty(list):
    assert list.is_empty()
    list.append(1)
    assert not list.is_empty()

def test_count_nodes(list):
    assert list.count() == 0
    list.append(1)
    assert list.count() == 1
    list.append(2)
    assert list.count() == 2
    list.append(3)
    assert list.count() == 3

def test_count_data(list):
    assert list.count(1) == 0
    list.append(1)
    assert list.count(1) == 1
    list.append(1)
    assert list.count(1) == 2
    list.append(1)
    assert list.count(1) == 3
    assert list.count(2) == 0
    assert list.count(None) == 3

def test_append(list):
    assert list.append(1) == 1
    assert list.append(2) == 2
    assert list.append(3) == 3
    assert list.to_array() == [1, 2, 3]

def test_prepend(list):
    assert list.prepend(1) == 1
    assert list.prepend(2) == 2
    assert list.prepend(3) == 3
    assert list.to_array() == [3, 2, 1]

def test_to_array(list):
    assert list.to_array() == []
    list.append(1)
    assert list.to_array() == [1]
    list.append(2)
    assert list.to_array() == [1, 2]
    list.append(3)
    assert list.to_array() == [1, 2, 3]
    list.prepend(4)
    assert list.to_array() == [4, 1, 2, 3]
    list.prepend(5)
    assert list.to_array() == [5, 4, 1, 2, 3]
    list.prepend(6)
    assert list.to_array() == [6, 5, 4, 1, 2, 3]

def test__str__(list):
    assert str(list) == ''
    list.append(1)
    assert str(list) == '1'
    list.append(2)
    assert str(list) == '1 -> 2'
    list.append(3)
    assert str(list) == '1 -> 2 -> 3'

def test_find_by_index(list):
    assert list.find_by_index(0) is None
    list.append(0)
    assert list.find_by_index(0) == 0
    list.append(1)
    assert list.find_by_index(1) == 1
    list.append(2)
    assert list.find_by_index(2) == 2
    assert list.find_by_index(3) is None
    assert list.find_by_index(-1) is None

def test_find_index_of(list):
    assert list.find_index_of(None) is None
    list.append(None)
    assert list.find_index_of(None) == 0
    list.append(1)
    assert list.find_index_of(1) == 1
    list.append(2)
    assert list.find_index_of(2) == 2
    list.append(3)
    assert list.find_index_of(3) == 3
    list.append(3)
    assert list.find_index_of(3) == 3
    assert list.find_index_of(4) is None

def test_insert_at_first_index(list):
    assert list.to_array() == []
    assert list.insert_at_index(0, 1)
    assert list.to_array() == [1]
    assert list.insert_at_index(0, 2)
    assert list.to_array() == [2, 1]
    assert list.insert_at_index(0, 3)
    assert list.to_array() == [3, 2, 1]

def test_insert_at_middle_index(small_list):
    assert small_list.to_array() == [1, 2, 3]
    assert small_list.insert_at_index(1, 4)
    assert small_list.to_array() == [1, 4, 2, 3]
    assert small_list.insert_at_index(2, 5)
    assert small_list.to_array() == [1, 4, 5, 2, 3]
    assert small_list.insert_at_index(2, 6)
    assert small_list.to_array() == [1, 4, 6, 5, 2, 3]

def test_insert_at_last_index(list):
    assert list.to_array() == []
    assert list.insert_at_index(0, 1)
    assert list.to_array() == [1]
    assert list.insert_at_index(1, 2)
    assert list.to_array() == [1, 2]
    assert list.insert_at_index(2, 3)
    assert list.to_array() == [1, 2, 3]

def test_insert_at_out_of_bounds_index(small_list):
    assert small_list.to_array() == [1, 2, 3]
    assert small_list.insert_at_index(-1, 1) == None
    assert small_list.to_array() == [1, 2, 3]
    assert small_list.insert_at_index(4, 1) == None
    assert small_list.to_array() == [1, 2, 3]

def test_delete_at_first_index(small_list):
    empty_list = List()
    assert empty_list.delete_at_index(0) == None

    assert small_list.to_array() == [1, 2, 3]
    assert small_list.delete_at_index(0) == 1
    assert small_list.to_array() == [2, 3]
    assert small_list.delete_at_index(0) == 2
    assert small_list.to_array() == [3]
    assert small_list.delete_at_index(0) == 3
    assert small_list.to_array() == []

def test_delete_at_middle_index(small_list):
    assert small_list.to_array() == [1, 2, 3]
    assert small_list.delete_at_index(1) == 2
    assert small_list.to_array() == [1, 3]

def test_delete_at_last_index(small_list):
    assert small_list.to_array() == [1, 2, 3]
    assert small_list.delete_at_index(2) == 3
    assert small_list.to_array() == [1, 2]
    assert small_list.delete_at_index(1) == 2
    assert small_list.to_array() == [1]
    assert small_list.delete_at_index(0) == 1
    assert small_list.to_array() == []

def test_delete_at_out_of_bounds_index(small_list):
    assert small_list.to_array() == [1, 2, 3]
    assert small_list.delete_at_index(3) == None
    assert small_list.to_array() == [1, 2, 3]
    assert small_list.delete_at_index(-1) == None
    assert small_list.to_array() == [1, 2, 3]

def test_delete_data_at_first_index(small_list):
    assert small_list.to_array() == [1, 2, 3]
    assert small_list.delete_data(1) == 1
    assert small_list.to_array() == [2, 3]
    assert small_list.delete_data(2) == 2
    assert small_list.to_array() == [3]
    assert small_list.delete_data(3) == 3
    assert small_list.to_array() == []

def test_delete_data_at_middle_index(small_list):
    assert small_list.to_array() == [1, 2, 3]
    assert small_list.delete_data(2)
    assert small_list.to_array() == [1, 3]

def test_delete_data_at_last_index(small_list):
    assert small_list.to_array() == [1, 2, 3]
    assert small_list.delete_data(3) == 3
    assert small_list.to_array() == [1, 2]
    assert small_list.delete_data(2) == 2
    assert small_list.to_array() == [1]
    assert small_list.delete_data(1) == 1
    assert small_list.to_array() == []

def test_delete_data_that_does_not_exist(small_list):
    assert small_list.to_array() == [1, 2, 3]
    assert small_list.delete_data(4) == None

def test_insert_into_list_with_empty_list(list, small_list):
    assert list.to_array() == []
    assert small_list.to_array() == [1, 2, 3]
    assert small_list.insert_list(0, list) == small_list
    assert small_list.to_array() == [1, 2, 3]
    assert list.to_array() == []

def test_insert_into_empty_list_with_list(list, small_list):
    assert list.to_array() == []
    assert small_list.to_array() == [1, 2, 3]
    assert list.insert_list(0, small_list) == list
    assert small_list.to_array() == [1, 2, 3]
    assert list.to_array() == []

def test_insert_list_at_front(small_list):
    list = List()
    list.append(10)
    list.append(11)
    list.append(12)
    assert list.to_array() == [10, 11, 12]
    assert small_list.insert_list(0, list) == small_list
    assert small_list.to_array() == [10, 11, 12, 1, 2, 3]

def test_insert_list_in_middle(small_list):
    list = List()
    list.append(10)
    list.append(11)
    list.append(12)
    assert list.to_array() == [10, 11, 12]
    assert small_list.insert_list(2, list) == small_list
    assert small_list.to_array() == [1, 2, 10, 11, 12, 3]

def test_insert_list_at_end(small_list):
    list = List()
    list.append(10)
    list.append(11)
    list.append(12)
    assert list.to_array() == [10, 11, 12]
    assert small_list.insert_list(3, list) == small_list
    assert small_list.to_array() == [1, 2, 3, 10, 11, 12]
    assert list.to_array() == [10, 11, 12]

def test_reverse(small_list):
    empty_list = List()
    assert empty_list.reverse().to_array() == []

    list_of_one = List()
    list_of_one.append(1)
    assert list_of_one.to_array() == [1]
    assert list_of_one.reverse().to_array() == [1]

    tiny_list = List()
    tiny_list.append(1)
    tiny_list.append(2)
    assert tiny_list.to_array() == [1, 2]
    assert tiny_list.reverse().to_array() == [2, 1]

    assert small_list.to_array() == [1, 2, 3]
    assert small_list.reverse().to_array() == [3, 2, 1]


def test_sort():
    list = List()
    assert list.sort().to_array() == []

    list.append(10)
    list.append(4)
    list.append(33)
    list.append(-8)
    assert list.to_array() == [10, 4, 33, -8]
    assert list.sort().to_array() == [-8, 4, 10, 33]
