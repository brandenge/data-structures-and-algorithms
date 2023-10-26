from data_structures.k_ary_tree_with_iteration import KaryTreeWithIteration as Tree
from fixtures.k_ary_trees_with_iteration import tree, small_tree, medium_tree

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
