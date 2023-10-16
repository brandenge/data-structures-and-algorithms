from data_structures.node import Node
from data_structures.queue import Queue

class KaryTreeWithRecursion:
    def __init__(self, k):
        self._root = None
        self.k = k

    def is_empty(self):
        return self._root is None

    def add(self, data):
        node = Node(data)
        if self.is_empty():
            self._root = node
            return data
        queue = Queue()
        queue.enqueue(self._root)

        def traverse_add():
            nonlocal queue
            if queue.is_empty(): return
            current = queue.dequeue()
            if len(current.children) < self.k:
                current.children.append(node)
                return data

            queue = current.enqueue_children(queue)
            traverse_add()

        traverse_add()
        return data

    def includes(self, data):
        if self.is_empty(): return False
        is_included = False

        def traverse_includes(current):
            if current.data == data:
                nonlocal is_included
                is_included = True
                return

            if len(current.children) > 0:
                current.traverse_children(traverse_includes)

        traverse_includes(self._root)
        return is_included

    def breadth_first_traversal(self):
        if self.is_empty(): return []

        # Need a queue to do BFS recursively
        queue = Queue()
        queue.enqueue(self._root)
        data = []

        def traverse_bfs():
            nonlocal queue
            if queue.is_empty(): return
            current = queue.dequeue()
            data.append(current.data)

            queue = current.enqueue_children(queue)
            traverse_bfs()

        traverse_bfs()
        return data

    def dfs_pre_order(self):
        if self.is_empty(): return []
        data = []

        def traverse_dfs_pre_order(current):
            data.append(current.data)
            current.traverse_children(traverse_dfs_pre_order)

        traverse_dfs_pre_order(self._root)
        return data

    def dfs_in_order(self):
        if self.is_empty(): return []
        data = []

        def traverse_dfs_in_order(current):
            if len(current.children) > 0: current.traverse_first_half_children(traverse_dfs_in_order)
            data.append(current.data)
            if len(current.children) > 2: current.traverse_second_half_children(traverse_dfs_in_order, (len(current.children) // 2) + 1)
            elif len(current.children) == 2: current.traverse_second_half_children(traverse_dfs_in_order, (len(current.children) // 2))

        traverse_dfs_in_order(self._root)
        return data

    def dfs_post_order(self):
        if self.is_empty(): return []
        data = []

        def traverse_dfs_post_order(current):
            current.traverse_children(traverse_dfs_post_order)
            data.append(current.data)

        traverse_dfs_post_order(self._root)
        return data
