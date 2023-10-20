from data_structures.node import Node
from data_structures.queue import Queue
from data_structures.stack import Stack

class Edge:
    def __init__(self, start_node, end_node = None, weight = 0):
        self._start_node = start_node
        self._end_node = end_node
        self._weight = weight

class GraphWithEdgeList:
    def __init__(self):
        self._edge_list = []

    def is_empty(self):
        return len(self._edge_list) == 0

    def get_nodes(self):
        return [edge._start_node for edge in self._edge_list if edge._end_node is None]

    def get_node_by_value(self, value):
        for edge in self._edge_list:
            if edge._start_node.data == value: return edge._start_node

    def add_node(self, data):
        node = Node(data)
        edge = Edge(node)
        self._edge_list.append(edge)
        return node

    def remove_node(self, target_node):
        for index, edge in enumerate(self._edge_list):
            if edge._start_node == target_node or edge._end_node == target_node:
                del self._edge_list[index]
        del target_node

    def remove_node_by_value(self, value):
        target_node = self.get_node_by_value(value)
        if target_node: self.remove_node(target_node)

    def add_edge(self, start_node, end_node, weight = 0):
        if self.are_connected(start_node, end_node):
            self.remove_edge(start_node, end_node)
        if start_node == end_node: return
        new_edge = Edge(start_node, end_node, weight)
        self._edge_list.append(new_edge)

    def remove_edge(self, start_node, end_node):
        for index, edge in enumerate(self._edge_list):
            if edge._start_node == start_node and edge._end_node == end_node:
                del self._edge_list[index]

    def node_count(self):
        return len(self.get_nodes())

    def edge_count(self):
        return len(self._edge_list) - self.node_count()

    def get_neighbors(self, node):
        return [edge._end_node for edge in self._edge_list if edge._start_node == node and edge._end_node is not None]

    def are_connected(self, start_node, end_node):
        for edge in self._edge_list:
            if edge._start_node == start_node and edge._end_node == end_node:
                return True
        return False

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
