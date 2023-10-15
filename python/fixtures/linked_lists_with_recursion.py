import pytest
from data_structures.linked_list_with_recursion import LinkedListWithRecursion as List

@pytest.fixture
def list():
    list = List()
    return list

@pytest.fixture
def small_list():
    list = List()
    list.append(1)
    list.append(2)
    list.append(3)
    return list