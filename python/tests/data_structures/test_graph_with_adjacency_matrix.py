import pytest
from data_structures.graph_with_adjacency_matrix import GraphWithAdjacencyMatrix as Graph
from fixtures.graphs_with_adjacency_matrix import small_graph

def test_initialization():
    graph = Graph()
    assert graph.is_empty()

def test_is_empty(small_graph):
    graph = Graph()
    assert graph.is_empty()
    assert not small_graph.is_empty()

def test_get_nodes(small_graph):
    graph = Graph()
    assert graph.get_nodes() == []
    assert [node.data for node in small_graph.get_nodes()] == [1, 2, 3, 4, 5]

def test_get_node_by_value():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    node4 = graph.add_node(4)
    node5 = graph.add_node(5)
    assert graph.get_node_by_value(1) == node1
    assert graph.get_node_by_value(2) == node2
    assert graph.get_node_by_value(3) == node3
    assert graph.get_node_by_value(4) == node4
    assert graph.get_node_by_value(5) == node5
    node6 = graph.add_node(5)
    assert graph.get_node_by_value(5) == node5
    assert graph.get_node_by_value(6) == None

def test_add_node():
    graph = Graph()
    assert graph.get_nodes() == []
    node1 = graph.add_node(1)
    assert graph.get_nodes() == [node1]
    node2 = graph.add_node(2)
    assert graph.get_nodes() == [node1, node2]
    node3 = graph.add_node(3)
    assert graph.get_nodes() == [node1, node2, node3]
    node4 = graph.add_node(4)
    assert graph.get_nodes() == [node1, node2, node3, node4]
    node5 = graph.add_node(5)
    assert graph.get_nodes() == [node1, node2, node3, node4, node5]

def test_remove_node():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    node4 = graph.add_node(4)
    node5 = graph.add_node(5)
    assert [node.data for node in graph.get_nodes()] == [1, 2, 3, 4, 5]
    graph.remove_node(node3)
    assert [node.data for node in graph.get_nodes()] == [1, 2, 4, 5]
    graph.remove_node(node1)
    assert [node.data for node in graph.get_nodes()] == [2, 4, 5]
    graph.remove_node(node5)
    assert [node.data for node in graph.get_nodes()] == [2, 4]
    graph.remove_node(node2)
    assert [node.data for node in graph.get_nodes()] == [4]
    graph.remove_node(node4)
    assert [node.data for node in graph.get_nodes()] == []
    graph.remove_node(node4)
    assert [node.data for node in graph.get_nodes()] == []

def test_remove_node_by_value(small_graph):
    assert [node.data for node in small_graph.get_nodes()] == [1, 2, 3, 4, 5]
    small_graph.remove_node_by_value(3)
    assert [node.data for node in small_graph.get_nodes()] == [1, 2, 4, 5]
    small_graph.remove_node_by_value(1)
    assert [node.data for node in small_graph.get_nodes()] == [2, 4, 5]
    small_graph.remove_node_by_value(5)
    assert [node.data for node in small_graph.get_nodes()] == [2, 4]
    small_graph.remove_node_by_value(2)
    assert [node.data for node in small_graph.get_nodes()] == [4]
    small_graph.remove_node_by_value(4)
    assert [node.data for node in small_graph.get_nodes()] == []
    small_graph.remove_node_by_value(4)
    assert [node.data for node in small_graph.get_nodes()] == []

def test_add_edge():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    graph.add_edge(node1, node2)
    assert graph.edge_count() == 1
    graph.add_edge(node1, node3)
    assert graph.edge_count() == 2
    graph.add_edge(node2, node3)
    assert graph.edge_count() == 3
    graph.add_edge(node2, node1)
    assert graph.edge_count() == 4
    graph.add_edge(node3, node1)
    assert graph.edge_count() == 5
    graph.add_edge(node3, node2)
    assert graph.edge_count() == 6
    graph.add_edge(node3, node2, 10)
    assert graph.edge_count() == 6

def test_remove_edge():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    assert graph.edge_count() == 0
    graph.remove_edge(node1, node2)
    assert graph.edge_count() == 0
    graph.add_edge(node1, node2)
    graph.add_edge(node1, node3)
    graph.add_edge(node2, node3)
    graph.add_edge(node2, node1)
    graph.add_edge(node3, node1)
    graph.add_edge(node3, node2)
    assert graph.edge_count() == 6
    graph.remove_edge(node1, node2)
    assert graph.edge_count() == 5
    graph.remove_edge(node1, node3)
    assert graph.edge_count() == 4
    graph.remove_edge(node2, node1)
    assert graph.edge_count() == 3
    graph.remove_edge(node2, node3)
    assert graph.edge_count() == 2
    graph.remove_edge(node3, node1)
    assert graph.edge_count() == 1
    graph.remove_edge(node3, node2)
    assert graph.edge_count() == 0

def test_node_count():
    graph = Graph()
    assert graph.node_count() == 0
    graph.add_node(1)
    assert graph.node_count() == 1
    graph.add_node(2)
    assert graph.node_count() == 2
    graph.add_node(3)
    assert graph.node_count() == 3
    graph.remove_node_by_value(3)
    assert graph.node_count() == 2
    graph.remove_node_by_value(2)
    assert graph.node_count() == 1
    graph.remove_node_by_value(1)
    assert graph.node_count() == 0

def test_edge_count():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    assert graph.edge_count() == 0
    graph.remove_edge(node1, node2)
    assert graph.edge_count() == 0
    graph.add_edge(node1, node2)
    assert graph.edge_count() == 1
    graph.add_edge(node1, node3)
    assert graph.edge_count() == 2
    graph.add_edge(node2, node3)
    assert graph.edge_count() == 3
    graph.add_edge(node2, node1)
    assert graph.edge_count() == 4
    graph.add_edge(node3, node1)
    assert graph.edge_count() == 5
    graph.add_edge(node3, node2)
    assert graph.edge_count() == 6
    graph.remove_edge(node1, node2)
    assert graph.edge_count() == 5
    graph.remove_edge(node1, node3)
    assert graph.edge_count() == 4
    graph.remove_edge(node2, node1)
    assert graph.edge_count() == 3
    graph.remove_edge(node2, node3)
    assert graph.edge_count() == 2
    graph.remove_edge(node3, node1)
    assert graph.edge_count() == 1
    graph.remove_edge(node3, node2)
    assert graph.edge_count() == 0
    graph.remove_edge(node3, node2)
    assert graph.edge_count() == 0

def test_get_neighbors():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    node4 = graph.add_node(4)
    graph.add_edge(node1, node2)
    graph.add_edge(node1, node3)
    graph.add_edge(node2, node1)
    graph.add_edge(node2, node3)
    graph.add_edge(node3, node1)
    graph.add_edge(node3, node2)
    assert graph.get_neighbors(node1) == [node2, node3]
    assert graph.get_neighbors(node2) == [node1, node3]
    assert graph.get_neighbors(node3) == [node1, node2]
    assert graph.get_neighbors(node4) == []

def test_are_connected():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    node4 = graph.add_node(4)
    graph.add_edge(node1, node2)
    graph.add_edge(node1, node3)
    graph.add_edge(node2, node1)
    graph.add_edge(node2, node3)
    graph.add_edge(node3, node1)
    graph.add_edge(node3, node2)
    assert graph.are_connected(node1, node2) is True
    assert graph.are_connected(node1, node3) is True
    assert graph.are_connected(node2, node1) is True
    assert graph.are_connected(node2, node3) is True
    assert graph.are_connected(node3, node1) is True
    assert graph.are_connected(node3, node2) is True
    assert graph.are_connected(node4, node1) is False
    assert graph.are_connected(node4, node2) is False
    assert graph.are_connected(node4, node3) is False
    assert graph.are_connected(node3, node3) is False

def test_breadth_first_traversal():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    node4 = graph.add_node(4)
    node5 = graph.add_node(5)
    graph.add_edge(node1, node2, 1)
    graph.add_edge(node1, node3, 2)
    graph.add_edge(node2, node3, 3)
    graph.add_edge(node2, node5, 5)
    graph.add_edge(node3, node4, 4)
    graph.add_edge(node4, node2, 1)
    graph.add_edge(node4, node5, 2)
    graph.add_edge(node5, node1, 6)
    graph.add_edge(node5, node3, 2)
    assert graph.breadth_first_traversal(node1) == [node1, node2, node3, node5, node4]
    assert graph.breadth_first_traversal(node2) == [node2, node3, node5, node4, node1]
    assert graph.breadth_first_traversal(node3) == [node3, node4, node2, node5, node1]
    assert graph.breadth_first_traversal(node4) == [node4, node2, node5, node3, node1]
    assert graph.breadth_first_traversal(node5) == [node5, node1, node3, node2, node4]

def test_depth_first_traversal():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = graph.add_node(3)
    node4 = graph.add_node(4)
    node5 = graph.add_node(5)
    graph.add_edge(node1, node2, 1)
    graph.add_edge(node1, node3, 2)
    graph.add_edge(node2, node3, 3)
    graph.add_edge(node2, node5, 5)
    graph.add_edge(node3, node4, 4)
    graph.add_edge(node4, node2, 1)
    graph.add_edge(node4, node5, 2)
    graph.add_edge(node5, node1, 6)
    graph.add_edge(node5, node3, 2)
    assert graph.depth_first_traversal(node1) == [node1, node3, node4, node5, node2]
    assert graph.depth_first_traversal(node2) == [node2, node5, node1, node3, node4]
    assert graph.depth_first_traversal(node3) == [node3, node4, node5, node1, node2]
    assert graph.depth_first_traversal(node4) == [node4, node5, node3, node1, node2]
    assert graph.depth_first_traversal(node5) == [node5, node3, node4, node2, node1]
