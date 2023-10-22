import pytest
from data_structures.graph_with_edge_list import GraphWithEdgeList as Graph

@pytest.fixture
def small_graph():
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
    return graph
