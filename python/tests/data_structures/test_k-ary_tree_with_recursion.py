from data_structures.k_ary_tree_with_recursion import KaryTreeWithRecursion as Tree
from fixtures.k_ary_trees_with_recursion import *

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

def test_find_node_to_delete_and_last_node(tree, small_tree, medium_tree):
    assert tree.find_node_to_delete_and_last_node(1) is None

    node_to_delete, last_node = small_tree.find_node_to_delete_and_last_node(1)
    assert node_to_delete == small_tree._root
    assert last_node.data == 9

    node_to_delete, last_node = medium_tree.find_node_to_delete_and_last_node(1)
    assert node_to_delete == medium_tree._root
    assert last_node.data == 51

    node_to_delete, last_node = medium_tree.find_node_to_delete_and_last_node(41)
    assert node_to_delete.data == 41
    assert last_node.data == 51

def test_delete(tree, small_tree):
    assert tree.delete(1) is None
    assert small_tree.breadth_first_traversal() == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert small_tree.delete(-1) is None
    assert small_tree.breadth_first_traversal() == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert small_tree.delete(1) == 1
    assert small_tree.breadth_first_traversal() == [9, 2, 3, 4, 5, 6, 7, 8]
    assert small_tree.delete(2) == 2
    assert small_tree.breadth_first_traversal() == [9, 8, 3, 4, 5, 6, 7]
    assert small_tree.delete(7) == 7
    assert small_tree.breadth_first_traversal() == [9, 8, 3, 4, 5, 6]
    assert small_tree.delete(6) == 6
    assert small_tree.breadth_first_traversal() == [9, 8, 3, 4, 5]
    assert small_tree.delete(3) == 3
    assert small_tree.breadth_first_traversal() == [9, 8, 5, 4]
    assert small_tree.delete(5) == 5
    assert small_tree.breadth_first_traversal() == [9, 8, 4]
    assert small_tree.delete(8) == 8
    assert small_tree.breadth_first_traversal() == [9, 4]
    assert small_tree.delete(9) == 9
    assert small_tree.breadth_first_traversal() == [4]
    assert small_tree.delete(4) == 4
    assert small_tree.breadth_first_traversal() == []
    assert small_tree.delete(4) is None
    assert small_tree.breadth_first_traversal() == []

def test_includes(tree, medium_tree):
    assert tree.includes(1) is False
    assert medium_tree.includes(4) is True
    assert medium_tree.includes(5) is True
    assert medium_tree.includes(6) is True
    assert medium_tree.includes(7) is True
    assert medium_tree.includes(0) is False
    assert medium_tree.includes(52) is False

def test_breadth_first_traversal(tree, small_tree, medium_tree):
    assert tree.breadth_first_traversal() == []
    assert small_tree.breadth_first_traversal() == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert medium_tree.breadth_first_traversal() == [n for n in range(1, 52)]

def test_dfs_pre_order(tree, small_tree, medium_tree):
    assert tree.dfs_pre_order() == []
    assert small_tree.dfs_pre_order() == [1, 2, 5, 6, 7, 3, 8, 9, 4]
    assert medium_tree.dfs_pre_order() == [1, 2, 7, 32, 33, 34, 35, 36, 8, 37, 38, 39, 40, 41, 9, 42, 43, 44, 45, 46, 10, 47, 48, 49, 50, 51, 11, 3, 12, 13, 14, 15, 16, 4, 17, 18, 19, 20, 21, 5, 22, 23, 24, 25, 26, 6, 27, 28, 29, 30, 31]

def test_dfs_in_order(tree, small_tree, medium_tree):
    assert tree.dfs_in_order() == []
    assert small_tree.dfs_in_order() == [5, 6, 2, 7, 8, 3, 9, 1, 4]
    assert medium_tree.dfs_in_order() == [32, 33, 34, 7, 35, 36, 37, 38, 39, 8, 40, 41, 42, 43, 44, 9, 45, 46, 2, 47, 48, 49, 10, 50, 51, 11, 12, 13, 14, 3, 15, 16, 17, 18, 19, 4, 20, 21, 1, 22, 23, 24, 5, 25, 26, 27, 28, 29, 6, 30, 31]

def test_dfs_post_order(tree, small_tree, medium_tree):
    assert tree.dfs_post_order() == []
    assert small_tree.dfs_post_order() == [5, 6, 7, 2, 8, 9, 3, 4, 1]
    assert medium_tree.dfs_post_order() == [32, 33, 34, 35, 36, 7, 37, 38, 39, 40, 41, 8, 42, 43, 44, 45, 46, 9, 47, 48, 49, 50, 51, 10, 11, 2, 12, 13, 14, 15, 16, 3, 17, 18, 19, 20, 21, 4, 22, 23, 24, 25, 26, 5, 27, 28, 29, 30, 31, 6, 1]
