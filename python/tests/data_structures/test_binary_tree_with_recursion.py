import pytest
from data_structures.binary_tree_with_recursion import BinaryTreeWithRecursion as Tree
from data_structures.node import Node

@pytest.fixture
def tree():
    return Tree()

@pytest.fixture
def small_tree():
    tree = Tree()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    root = node1
    tree._root = root
    root.left = node2
    root.right = node3
    return tree

@pytest.fixture
def medium_tree():
    tree = Tree()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    root = node1
    tree._root = root
    root.left = node2
    root.right = node3
    root.left.left = node4
    root.left.right = node5
    root.right.left = node6
    root.right.right = node7
    return tree

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

def contains(tree, small_tree):
    assert tree.includes(1) is False
    assert small_tree.includes(1) is True
    assert small_tree.includes(2) is True
    assert small_tree.includes(3) is True
    assert small_tree.includes(0) is False
    assert small_tree.includes(4) is False

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
