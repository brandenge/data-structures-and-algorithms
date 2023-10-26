from data_structures.binary_search_tree_with_iteration import BinarySearchTreeWithIteration as Tree
from fixtures.binary_search_trees_with_iteration import tree, small_tree, medium_tree

def test_initialization(tree):
    assert tree.is_empty()

def test_add(tree):
    assert tree.breadth_first_traversal() == []
    assert tree.add(0) == 0
    assert tree.breadth_first_traversal() == [0]
    assert tree.add(-10) == -10
    assert tree.breadth_first_traversal() == [0, -10]
    assert tree.add(10) == 10
    assert tree.breadth_first_traversal() == [0, -10, 10]
    assert tree.add(-20) == -20
    assert tree.breadth_first_traversal() == [0, -10, 10, -20]
    assert tree.add(20) == 20
    assert tree.breadth_first_traversal() == [0, -10, 10, -20, 20]
    assert tree.add(-5) == -5
    assert tree.breadth_first_traversal() == [0, -10, 10, -20, -5, 20]
    assert tree.add(5) == 5
    assert tree.breadth_first_traversal() == [0, -10, 10, -20, -5, 5, 20]
    assert tree.add(15) == 15
    assert tree.breadth_first_traversal() == [0, -10, 10, -20, -5, 5, 20, 15]
    assert tree.add(-15) == -15
    assert tree.breadth_first_traversal() == [0, -10, 10, -20, -5, 5, 20, -15, 15]

def test_includes(tree, medium_tree):
    assert tree.includes(0) is False
    assert medium_tree.includes(0) is True
    assert medium_tree.includes(-10) is True
    assert medium_tree.includes(10) is True
    assert medium_tree.includes(-5) is True
    assert medium_tree.includes(-15) is True
    assert medium_tree.includes(15) is True
    assert medium_tree.includes(-1) is False
    assert medium_tree.includes(82) is False

def test_breadth_first_traversal(tree, small_tree, medium_tree):
    assert tree.breadth_first_traversal() == []
    assert small_tree.breadth_first_traversal() == [0, -10, 10]
    assert medium_tree.breadth_first_traversal() == [0, -10, 10, -15, -5, 5, 15]

def test_dfs_pre_order_alternative(tree, small_tree, medium_tree):
    assert tree.dfs_pre_order_alternative() == []
    assert small_tree.dfs_pre_order_alternative() == [0, -10, 10]
    assert medium_tree.dfs_pre_order_alternative() == [0, -10, -15, -5, 10, 5, 15]

def test_dfs_pre_order(tree, small_tree, medium_tree):
    assert tree.dfs_pre_order() == []
    assert small_tree.dfs_pre_order() == [0, -10, 10]
    assert medium_tree.dfs_pre_order() == [0, -10, -15, -5, 10, 5, 15]

def test_dfs_in_order(tree, small_tree, medium_tree):
    assert tree.dfs_in_order() == []
    assert small_tree.dfs_in_order() == [-10, 0, 10]
    assert medium_tree.dfs_in_order() == [-15, -10, -5, 0, 5, 10, 15]

def test_dfs_post_order(tree, small_tree, medium_tree):
    assert tree.dfs_post_order() == []
    assert small_tree.dfs_post_order() == [-10, 10, 0]
    assert medium_tree.dfs_post_order() == [-15, -5, -10, 5, 15, 10, 0]

def test_dfs_post_order_two_stacks(tree, small_tree, medium_tree):
    assert tree.dfs_post_order_two_stacks() == []
    assert small_tree.dfs_post_order_two_stacks() == [-10, 10, 0]
    assert medium_tree.dfs_post_order_two_stacks() == [-15, -5, -10, 5, 15, 10, 0]
