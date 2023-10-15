import pytest
from data_structures.binary_search_tree_with_iteration import BinarySearchTreeWithIteration as Tree
from fixtures.binary_search_trees_with_iteration import tree, small_tree, medium_tree

def test_exists(tree):
    assert tree

def test_initialization(tree):
    assert tree.is_empty()

def test_add(tree):
    assert tree.breadth_first_traversal() == []
    tree.add(1)
    assert tree.breadth_first_traversal() == [1]
    tree.add(2)
    assert tree.breadth_first_traversal() == [1, 2]
    tree.add(3)
    assert tree.breadth_first_traversal() == [1, 2, 3]
    tree.add(4)
    assert tree.breadth_first_traversal() == [1, 2, 3, 4]
    tree.add(5)
    assert tree.breadth_first_traversal() == [1, 2, 3, 4, 5]
    tree.add(6)
    assert tree.breadth_first_traversal() == [1, 2, 3, 4, 5, 6]
    tree.add(7)
    assert tree.breadth_first_traversal() == [1, 2, 3, 4, 5, 6, 7]

def test_includes(tree, small_tree):
    assert tree.includes(1) is False
    assert small_tree.includes(1) is True
    assert small_tree.includes(2) is True
    assert small_tree.includes(3) is True
    assert small_tree.includes(0) is False
    assert small_tree.includes(4) is False
