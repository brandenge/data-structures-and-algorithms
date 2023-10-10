import pytest
from data_structures.linked_list_with_iteration import LinkedListWithIteration as List, Node, LinkedListCycleError


@pytest.fixture()
def list():
    list = List()
    for i in range(5):
        list.append(i)
    return list


def test_exists():
    assert List


def test_initialization(list):
    list = List()
    assert list.is_valid()


def test_append():
    list = List()
    for i in range(5):
        assert list.append(i) == i
        assert list.is_valid()


def test_prepend():
    list = List()
    for i in range(5):
        assert list.prepend(i) == i
        assert list.is_valid()
    

def test_last():
    list = List()
    assert list.last() == None
    assert list.is_valid()
    for i in range(5):
        list.append(i)
        assert list.last() == i
        assert list.is_valid()


def test_count():
    list = List()
    assert list.count() == 0
    assert list.is_valid()
    for i in range(5):
        list.append(i)
        assert list.count() == i + 1
        assert list.is_valid()


def test_to_array():
    list = List()
    array = []
    assert list.to_array() == array
    assert list.is_valid()
    for i in range(5):
        list.append(i)
        array += [i]
        assert list.to_array() == array
        assert list.is_valid()


def test_to_array_with_nodes(list):
    array = []
    current = list.head
    while current:
        array.append(current)
        current = current.next

    assert list.to_array(nodes = True) == array
    assert list.is_valid()


def test_has_cycle_false(list):
    assert not list.has_cycle()
    assert list.is_valid()


def test_has_cycle_true(list):
    list.tail.next = list.head
    assert list.has_cycle()
    assert not list.is_valid()


def test_is_valid_empty_list_true():
    list = List()
    assert list.is_valid()


def test_is_valid_empty_list_false():
    list = List()
    list.tail = 5
    assert not list.is_valid()


def test_is_valid_count_true(list):
    assert list.is_valid()


def test_is_valid_count_false(list):
    list._length = 10
    assert not list.is_valid()


def test_is_valid_head_true(list):
    assert list.is_valid()


def test_is_valid_head_false(list):
    list.head = list.head.next
    assert not list.is_valid()

    node = Node(5)
    list.head = node
    assert not list.is_valid()

    list.head = True
    assert not list.is_valid()


def test_is_valid_tail_true(list):
    assert list.is_valid()


def test_is_valid_tail_false(list):
    list.tail = list.head.next
    assert not list.is_valid()

    list.tail = Node(5)
    assert not list.is_valid()

    list.tail = True
    assert not list.is_valid()


def test_is_valid_tail_next_true(list):
    assert list.is_valid()


def test_is_valid_tail_next_false(list):
    list.tail.next = True
    assert not list.is_valid()

    list.tail.next = False
    assert not list.is_valid()


def test_count_value():
    list = List()
    assert list.count_value(0) == 0
    assert list.is_valid()
    for i in range(5):
        list.append(0)
        assert list.count_value(0) == i + 1
        assert list.is_valid()

  
def test_find_index_of(list):
    for i in range(5):
        assert list.find_index_of(i) == i
        assert list.is_valid()


def test_find_index_of_value_that_does_not_exist():
    list = List()
    assert list.find_index_of(0) == None
    assert list.is_valid()
    
    for i in range(5):
        list.append(i)

    for i in range(5, 10):
        assert list.find_index_of(i) == None
        assert list.is_valid()


def test_find_value_at(list):
    for i in range(5):
        assert list.find_value_at(i) == i
        assert list.is_valid()


def test_find_value_at_index_that_does_not_exist():
    list = List()
    assert list.find_value_at(0) == None
    assert list.is_valid()

    for i in range(5):
        list.append(i)

    for i in range(5, 10):
        assert list.find_value_at(i) == None
        assert list.is_valid()

    for i in range(-1, -6, -1):
        assert list.find_value_at(i) == None
        assert list.is_valid()


def find_prev_node_of_index():
    nodes = list.to_array(nodes = True)
    for i in range(1, 5):
        assert find_prev_node_of_index(i) == nodes[i - 1]


def test_insert_at_position_at_first_index():
    list = List()
    for i in range(5):
        assert list.insert_at_position(0, i) == i
        assert list.is_valid()


def test_insert_at_position_at_middle_index():
    list = List()

    for i in range(5):
        list.append(i)

    for i in range(5):
        assert list.insert_at_position(2, i + 10) == i + 10
        assert list.is_valid()


def test_insert_at_position_at_last_index():
    list = List()
    
    for i in range(5):
        assert list.insert_at_position(i, i) == i
        assert list.is_valid()


def test_insert_at_position_with_out_of_bounds_index(list):
    for i in range(6, 10):
        assert list.insert_at_position(i, i) == None
        assert list.is_valid()

    for i in range(-1, -6, -1):
        assert list.insert_at_position(i, i) == None
        assert list.is_valid()


def test_delete_at_position_at_first_index(list):
    for i in range(5):
        assert list.delete_at_position(0) == i
        assert list.is_valid()

    assert list.delete_at_position(0) == None
    assert list.is_valid()


def test_delete_at_position_at_middle_index(list):
    for i in range(2, 5):
        assert list.delete_at_position(2) == i
        assert list.is_valid()

    assert list.delete_at_position(2) == None
    assert list.is_valid()
    

def test_delete_at_position_at_last_index(list):
    for i in range(4, -1, -1):
        assert list.delete_at_position(i) == i
        assert list.is_valid()

    assert list.delete_at_position(0) == None
    assert list.is_valid()


def test_delete_at_position_with_out_of_bounds_index(list):
    for i in range(5, 10):
        assert list.delete_at_position(i) == None
        assert list.is_valid()

    for i in range(-1, -6, -1):
        assert list.delete_at_position(i) == None
        assert list.is_valid()


def test_delete_value_at_head(list):
    for i in range(5):
        assert list.delete_value(i) == i
        assert list.is_valid()

    assert list.delete_at_position(0) == None
    assert list.is_valid()


def test_delete_value_at_middle(list):
    for i in range(2, 5):
        assert list.delete_value(i) == i
        assert list.is_valid()

    assert list.delete_value(2) == None
    assert list.is_valid()


def test_delete_value_at_last(list):
    for i in range(4, -1, -1):
        assert list.delete_value(i) == i
        assert list.is_valid()

    assert list.delete_value(0) == None
    assert list.is_valid()


def test_delete_value_when_value_does_not_exist():
    list = List()
    assert list.delete_value(0) == None
    assert list.is_valid()

    for i in range(5):
        list.append(i)

    for i in range(5, 10):
        assert list.delete_value(i) == None
        assert list.is_valid()

    for i in range(-1, -6, -1):
        assert list.delete_value(i) == None
        assert list.is_valid()


def test_insert_list_with_empty_list(list):
    empty_list = List()
    assert list.insert_list(0, empty_list) == list
    assert list.to_array() == [0, 1, 2, 3, 4]
    assert list.is_valid()
    assert empty_list.to_array() == []
    assert empty_list.is_valid()


def test_insert_empty_list_with_list(list):
    empty_list = List()
    assert empty_list.insert_list(0, list) == empty_list
    assert empty_list.to_array() == [0, 1, 2, 3, 4]
    assert empty_list.is_valid()
    assert list.to_array() == [0, 1, 2, 3, 4]
    assert list.is_valid()


def test_insert_list_at_front(list):
    list2 = List()
    for i in range(3):
        list2.append(i + 10)

    assert list.insert_list(0, list2) == list
    assert list.to_array() == [10, 11, 12, 0, 1, 2, 3, 4]
    assert list.is_valid()
    assert list2.to_array() == [10, 11, 12]
    assert list2.is_valid()


def test_insert_list_in_middle(list):
    list2 = List()
    for i in range(3):
        list2.append(i + 10)

    assert list.insert_list(2, list2) == list
    assert list.to_array() == [0, 1, 10, 11, 12, 2, 3, 4]
    assert list.is_valid()
    assert list2.to_array() == [10, 11, 12]
    assert list2.is_valid()


def test_insert_list_at_end(list):
    list2 = List()
    for i in range(3):
        list2.append(i + 10)

    assert list.insert_list(0, list2) == list
    assert list.to_array() == [10, 11, 12, 0, 1, 2, 3, 4]
    assert list.is_valid()
    assert list2.to_array() == [10, 11, 12]
    assert list2.is_valid()


def test_reverse(list):
    empty_list = List()
    assert empty_list.reverse().to_array() == []
    assert empty_list.is_valid()
    
    assert list.reverse().to_array() == [4, 3, 2, 1, 0]
    assert list.is_valid()


def test_sort():
    list = List()
    assert list.sort().to_array() == []
    assert list.is_valid()
    
    list.append(10)
    list.append(4)
    list.append(33)
    list.append(-8)
    sorted_list = list.sort()

    assert sorted_list.to_array() == [-8, 4, 10, 33]
    assert list.is_valid()
    assert sorted_list.is_valid()