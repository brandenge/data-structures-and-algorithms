import pytest
from data_structures.binary_search_tree_with_recursion import BinarySearchTreeWithRecursion as Tree

@pytest.fixture
def tree():
    return Tree()

@pytest.fixture
def small_tree():
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    return tree

@pytest.fixture
def medium_tree():
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    return tree
