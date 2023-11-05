from data_structures.binary_tree_with_recursion import BinaryTreeWithRecursion as Tree
from fixtures.binary_trees_with_recursion import *

def test_initialization(tree):
    assert tree.is_empty()

def test_add(tree):
    assert tree.breadth_first_traversal() == []
    assert tree.add(1) == 1
    assert tree.breadth_first_traversal() == [1]
    assert tree.add(2) == 2
    assert tree.breadth_first_traversal() == [1, 2]
    assert tree.add(3) == 3
    assert tree.breadth_first_traversal() == [1, 2, 3]
    assert tree.add(4) == 4
    assert tree.breadth_first_traversal() == [1, 2, 3, 4]
    assert tree.add(5) == 5
    assert tree.breadth_first_traversal() == [1, 2, 3, 4, 5]
    assert tree.add(6) == 6
    assert tree.breadth_first_traversal() == [1, 2, 3, 4, 5, 6]
    assert tree.add(7) == 7
    assert tree.breadth_first_traversal() == [1, 2, 3, 4, 5, 6, 7]

def test_delete(tree, medium_tree):
    assert tree.delete(1) is None
    assert medium_tree.breadth_first_traversal() == [1, 2, 3, 4, 5, 6, 7]
    assert medium_tree.delete(-1) is None
    assert medium_tree.breadth_first_traversal() == [1, 2, 3, 4, 5, 6, 7]
    assert medium_tree.delete(1) == 1
    assert medium_tree.breadth_first_traversal() == [7, 2, 3, 4, 5, 6]
    assert medium_tree.delete(2) == 2
    assert medium_tree.breadth_first_traversal() == [7, 6, 3, 4, 5]
    assert medium_tree.delete(3) == 3
    assert medium_tree.breadth_first_traversal() == [7, 6, 5, 4]
    assert medium_tree.delete(6) == 6
    assert medium_tree.breadth_first_traversal() == [7, 4, 5]
    assert medium_tree.delete(5) == 5
    assert medium_tree.breadth_first_traversal() == [7, 4]
    assert medium_tree.delete(7) == 7
    assert medium_tree.breadth_first_traversal() == [4]
    assert medium_tree.delete(4) == 4
    assert medium_tree.breadth_first_traversal() == []
    assert medium_tree.delete(4) is None
    assert medium_tree.breadth_first_traversal() == []

def test_includes(tree, medium_tree):
    assert tree.includes(1) is False
    assert medium_tree.includes(4) is True
    assert medium_tree.includes(5) is True
    assert medium_tree.includes(6) is True
    assert medium_tree.includes(7) is True
    assert medium_tree.includes(0) is False
    assert medium_tree.includes(10) is False

def test_breadth_first_traversal(tree, small_tree, medium_tree):
    assert tree.breadth_first_traversal() == []
    assert small_tree.breadth_first_traversal() == [1, 2, 3]
    assert medium_tree.breadth_first_traversal() == [1, 2, 3, 4, 5, 6, 7]

def test_dfs_pre_order(tree, small_tree, medium_tree):
    assert tree.dfs_pre_order() == []
    assert small_tree.dfs_pre_order() == [1, 2, 3]
    assert medium_tree.dfs_pre_order() == [1, 2, 4, 5, 3, 6, 7]

def test_dfs_in_order(tree, small_tree, medium_tree):
    assert tree.dfs_in_order() == []
    assert small_tree.dfs_in_order() == [2, 1, 3]
    assert medium_tree.dfs_in_order() == [4, 2, 5, 1, 6, 3, 7]

def test_dfs_post_order(tree, small_tree, medium_tree):
    assert tree.dfs_post_order() == []
    assert small_tree.dfs_post_order() == [2, 3, 1]
    assert medium_tree.dfs_post_order() == [4, 5, 2, 6, 7, 3, 1]

def test_find_height(tree, small_tree, medium_tree):
    assert tree.find_height() == 0
    assert small_tree.find_height() == 2
    assert medium_tree.find_height() == 3

def test_is_balanced(tree, small_tree, medium_tree, unbalanced_tree):
    assert tree.is_balanced() is True
    assert small_tree.is_balanced() is True
    assert medium_tree.is_balanced() is True
    assert unbalanced_tree.is_balanced() is False
