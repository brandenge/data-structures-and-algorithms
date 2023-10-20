import pytest
from data_structures.node import Node

@pytest.fixture
def node():
    return Node()

@pytest.fixture
def nodes():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    return [node1, node2, node3]
