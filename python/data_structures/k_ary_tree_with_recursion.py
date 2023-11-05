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

            current.enqueue_children(queue)
            traverse_add()

        traverse_add()
        return data

    def find_node_to_delete_and_last_node(self, data):
        if self.is_empty(): return
        node_to_delete = None
        # Need queue for using BFS traversal to find last node
        queue = Queue()
        queue.enqueue(self._root)

        def traverse_find_delete_and_last_node():
            nonlocal node_to_delete
            if queue.is_empty(): return
            current = queue.dequeue()
            if current.data == data: node_to_delete = current
            current.enqueue_children(queue)
            if queue.is_empty(): return [node_to_delete, current]
            return traverse_find_delete_and_last_node()

        return traverse_find_delete_and_last_node()

    def find_parent(self, target):
        # If the root node is the target, it does not have a parent
        if self.is_empty() or target is None or target == self._root: return

        # Using pass-by-reference data types here so that the nested function
        # has access and behaves like a normal closure without the need for the
        # nonlocal keyword in the nested function
        parent_node = [None]
        target_idx = [None]
        target = [target]

        def traverse_find_parent(parent, child_idx = 0):
            if parent_node[0] is not None: return
            if child_idx >= len(parent.children): return
            child = parent.children[child_idx]
            if child == target[0]:
                parent_node[0] = parent
                target_idx[0] = child_idx
                return

            if child_idx + 1 < len(parent.children):
                # Iterate through the children of the child parent
                # keep the same parent, increment the index to get the next child
                traverse_find_parent(parent, child_idx + 1)
            # Set the child node as the new parent to traverse deeper
            traverse_find_parent(child)

        traverse_find_parent(self._root)
        return [parent_node[0], target_idx[0]]

    def delete(self, data):
        if self.is_empty(): return
        # If the root node is the last node in the tree
        if len(self._root.children) == 0:
            if self._root.data == data:
                self._root = None
                return data
            else:
                return

        node_to_delete, last_node = self.find_node_to_delete_and_last_node(data)
        if node_to_delete is None: return
        parent_of_last_node, last_node_idx = self.find_parent(last_node)
        node_to_delete.data = last_node.data

        parent_children = []
        def remove_last_node(idx = 0):
            nonlocal last_node
            nonlocal parent_of_last_node
            nonlocal parent_children
            if idx != last_node_idx:
                parent_children.append(parent_of_last_node.children[idx])
            if parent_of_last_node and idx + 1 < len(parent_of_last_node.children):
                remove_last_node(idx + 1)

        remove_last_node()
        if parent_of_last_node: parent_of_last_node.children = parent_children

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
