import pytest
from data_structures.binary_tree_with_recursion import BinaryTreeWithRecursion as Tree
from data_structures.node import Node

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

@pytest.fixture
def unbalanced_tree():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node4.left = node5
    tree = Tree()
    tree._root = node1
    return tree
