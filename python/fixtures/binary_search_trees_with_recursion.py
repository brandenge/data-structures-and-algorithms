import pytest
from data_structures.binary_search_tree_with_recursion import BinarySearchTreeWithRecursion as Tree

@pytest.fixture
def tree():
    return Tree()

@pytest.fixture
def small_tree():
    tree = Tree()
    tree.add(0)
    tree.add(-10)
    tree.add(10)
    return tree

@pytest.fixture
def medium_tree():
    tree = Tree()
    tree.add(0)
    tree.add(-10)
    tree.add(10)
    tree.add(-5)
    tree.add(5)
    tree.add(-15)
    tree.add(15)
    return tree
