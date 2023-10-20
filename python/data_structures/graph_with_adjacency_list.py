from data_structures.node import Node
from data_structures.queue import Queue
from data_structures.stack import Stack

class Edge:
    def __init__(self, node, weight = 0):
        self._node = node
        self._weight = weight

class GraphWithAdjacencyList:
    def __init__(self):
        self._adjacency_list = {}

    def is_empty(self):
        return len(self._adjacency_list) == 0

    def get_nodes(self):
        return [*self._adjacency_list.keys()]

    def get_node_by_value(self, value):
        for node in self._adjacency_list:
            if node.data == value: return node

    def add_node(self, data):
        node = Node(data)
        self._adjacency_list[node] = []
        return node

    def remove_node(self, target_node):
        if target_node not in self._adjacency_list: return
        for node in self._adjacency_list:
            self.remove_edge(node, target_node)
        del self._adjacency_list[target_node]

    def remove_node_by_value(self, value):
        target_node = self.get_node_by_value(value)
        if target_node: self.remove_node(target_node)

    def add_edge(self, start_node, end_node, weight = 0):
        if self.are_connected(start_node, end_node):
            self.remove_edge(start_node, end_node)
        if start_node == end_node: return
        self._adjacency_list[start_node] += [Edge(end_node, weight)]

    def remove_edge(self, start_node, end_node):
        edges = self._adjacency_list[start_node]
        edges = [edge for edge in edges if edge._node != end_node ]
        self._adjacency_list[start_node] = edges

    def node_count(self):
        return len(self.get_nodes())

    def edge_count(self):
        total = 0
        for node in self._adjacency_list:
            total += len(self._adjacency_list[node])
        return total

    def get_neighbors(self, node):
        return [edge._node for edge in self._adjacency_list[node]]

    def are_connected(self, start_node, end_node):
        return end_node in self.get_neighbors(start_node)

    def breadth_first_traversal(self, start_node = None):
        if self.is_empty() or start_node is None: return []
        queue = Queue()
        queue.enqueue(start_node)
        visited = set()
        visited.add(start_node)
        data = []

        while not queue.is_empty():
            current = queue.dequeue()
            data.append(current)
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
        return data

    def depth_first_traversal(self, start_node = None):
        if self.is_empty() or start_node is None: return []
        stack = Stack()
        stack.push(start_node)
        visited = set()
        visited.add(start_node)
        data = []

        while not stack.is_empty():
            current = stack.pop()
            data.append(current)
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    stack.push(neighbor)
                    visited.add(neighbor)
        return data
