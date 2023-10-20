from data_structures.node import Node
from data_structures.queue import Queue
from data_structures.stack import Stack

# Edge class removed compared to graph implementation using adjacency list because we can just store the weight now as the value of the start node and end node in the matrix.

class GraphWithAdjacencyMatrix:
    def __init__(self):
        self._adjacency_matrix = {}

    def is_empty(self):
        return self._adjacency_matrix == {}

    def get_nodes(self):
        return [*self._adjacency_matrix.keys()]

    def get_node_by_value(self, value):
        nodes = self.get_nodes()
        for node in nodes:
            if node.data == value: return node

    def add_node(self, data):
        node = Node(data)
        self._adjacency_matrix[node] = {}
        return node

    def remove_node(self, target_node):
        if target_node not in self.get_nodes(): return
        for node in self._adjacency_matrix:
            self.remove_edge(node, target_node)
        del self._adjacency_matrix[target_node]

    def remove_node_by_value(self, value):
        target_node = self.get_node_by_value(value)
        if target_node: self.remove_node(target_node)

    def add_edge(self, start_node, end_node, weight = 0):
        if self.are_connected(start_node, end_node):
            self.remove_edge(start_node, end_node)
        if start_node == end_node: return
        self._adjacency_matrix[start_node][end_node] = weight

    def remove_edge(self, start_node, end_node):
        if self.are_connected(start_node, end_node):
            del self._adjacency_matrix[start_node][end_node]

    def node_count(self):
        return len(self.get_nodes())

    def edge_count(self):
        total = 0
        for node in self._adjacency_matrix:
            total += len(self._adjacency_matrix[node])
        return total

    def get_neighbors(self, node):
        return [neighbor for neighbor in self._adjacency_matrix[node]]

    def are_connected(self, start_node, end_node):
        if (start_node in self._adjacency_matrix and
            end_node in self._adjacency_matrix[start_node]):
            return True
        else: return False

    def breadth_first_traversal(self, start_node = None):
        if self.is_empty() or start_node is None: return []
        queue = Queue()
        queue.enqueue(start_node)
        visited = set()
        data = []

        while not queue.is_empty():
            current = queue.dequeue()
            data.append(current)
            visited.add(current)
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
        data = []

        while not stack.is_empty():
            current = stack.pop()
            data.append(current)
            visited.add(current)
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    stack.push(neighbor)
                    visited.add(neighbor)
        return data
