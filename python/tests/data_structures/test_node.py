from data_structures.node import Node
from fixtures.node import node, nodes

def test_initialization():
    node1 = Node()
    assert node1.data == None
    assert node1.next == None
    node2 = Node(1)
    assert node2.data == 1
    assert node2.next == None

def test_properties(node):
    assert node.data is None
    assert node.next is None
    assert node.left is None
    assert node.right is None

def test_setters(node):
    assert node.next is None
    node2 = Node(5)
    node3 = Node(10)
    node.next = node2
    assert node.next == node2
    node.left = node2
    node.right = node3
    assert node.left == node2
    assert node.right == node3

def test_count_nodes():
    node1 = Node()
    assert node1.count() == 1
    node2 = Node()
    node1.next = node2
    assert node1.count() == 2
    node3 = Node()
    node2.next = node3
    assert node1.count() == 3
    assert node2.count() == 2
    assert node3.count() == 1

def test_count_data():
    node1 = Node(1)
    node2 = Node(1)
    node3 = Node(1)
    node1.next = node2
    node2.next = node3
    assert node1.to_array([]) == [1, 1, 1]
    assert node1.count(1) == 3
    assert node2.count(1) == 2
    assert node3.count(1) == 1
    assert node1.count(2) == 0

def test_find_by_index(nodes):
    node1, node2, node3 = nodes
    assert node1.to_array([]) == [1, 2, 3]
    assert node1.find_by_index(0) == 1
    assert node1.find_by_index(1) == 2
    assert node1.find_by_index(2) == 3

def test_find_index_of(nodes):
    node1, node2, node3 = nodes
    assert node1.to_array([]) == [1, 2, 3]
    assert node1.find_index_of(1) == 0
    assert node1.find_index_of(2) == 1
    assert node1.find_index_of(3) == 2

def test_to_array(nodes):
    node1, node2, node3 = nodes
    assert node1.to_array([]) == [1, 2, 3]
    assert node2.to_array([]) == [2, 3]
    assert node3.to_array([]) == [3]

def test_insert_at_middle_index(nodes):
    node1, node2, node3 = nodes
    assert node1.to_array([]) == [1, 2, 3]
    assert node1.insert_at_index(1, 10) == 10
    assert node1.to_array([]) == [1, 10, 2, 3]
    assert node1.insert_at_index(2, 11) == 11
    assert node1.to_array([]) == [1, 10, 11, 2, 3]
    assert node1.insert_at_index(2, 12) == 12
    assert node1.to_array([]) == [1, 10, 12, 11, 2, 3]

def test_insert_at_last_index(nodes):
    node1, node2, node3 = nodes
    assert node1.to_array([]) == [1, 2, 3]
    assert node1.insert_at_index(3, 10) == 10
    assert node1.to_array([]) == [1, 2, 3, 10]
    assert node1.insert_at_index(4, 11) == 11
    assert node1.to_array([]) == [1, 2, 3, 10, 11]
    assert node1.insert_at_index(5, 12) == 12
    assert node1.to_array([]) == [1, 2, 3, 10, 11, 12]

def test_get_previous_node_by_index(nodes):
    node1, node2, node3 = nodes
    assert node1.to_array([]) == [1, 2, 3]
    assert node1._get_previous_node_by_index(1) == node1
    assert node1._get_previous_node_by_index(2) == node2
    assert node1._get_previous_node_by_index(3) == node3

def test_reverse(nodes):
    node1, node2, node3 = nodes
    assert node1.to_array([]) == [1, 2, 3]
    assert node2.to_array([]) == [2, 3]
    assert node3.to_array([]) == [3]
    assert node1.reverse(None) == None
    assert node3.to_array([]) == [3, 2, 1]
    assert node2.to_array([]) == [2, 1]
    assert node1.to_array([]) == [1]
