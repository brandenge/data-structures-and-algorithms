from data_structures.node import Node
from data_structures.queue import Queue
from data_structures.stack import Stack

class KaryTreeWithIteration:
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
        while not queue.is_empty():
            current = queue.dequeue()
            if len(current.children) < self.k:
                current.children.append(node)
                return data
            else:
                for child in current.children:
                    queue.enqueue(child)

    def find_parent(self, target):
        if self.is_empty() or self._root == target: return
        queue = Queue()
        queue.enqueue(self._root)
        while not queue.is_empty():
            current = queue.dequeue()
            for idx, child in enumerate(current.children):
                if child == target: return [current, idx]
                else: queue.enqueue(child)

    def find_node_to_delete_and_last_node(self, data_to_delete):
        if self.is_empty(): return
        node_to_delete = None
        queue = Queue()
        queue.enqueue(self._root)
        while not queue.is_empty():
            current = queue.dequeue()
            if current.data == data_to_delete: node_to_delete = current
            for idx, child in enumerate(current.children):
                queue.enqueue(child)
            if queue.is_empty(): return [node_to_delete, current]

    # Simple implementation that swaps the deleted node with the last node
    def delete(self, data):
        if self.is_empty(): return
        node_to_delete, last_node = self.find_node_to_delete_and_last_node(data)
        parent_info = self.find_parent(last_node)

        # The last_node is the root, i.e. there is only one node in the tree
        if parent_info is None:
            self._root = None
            return data

        parent_of_last_node, last_node_idx = parent_info
        if node_to_delete:
            node_to_delete.data = last_node.data

            # To delete the last node, recreate it's parent's list of children
            # And re-assign it
            parent_children = []
            for idx, child in enumerate(parent_of_last_node.children):
                if idx != last_node_idx: parent_children.append(child)
            parent_of_last_node.children = parent_children
            return data

    def includes(self, data):
        if self.is_empty(): return False
        queue = Queue()
        queue.enqueue(self._root)
        while not queue.is_empty():
            current = queue.dequeue()
            if current.data == data: return True
            for child in current.children:
                queue.enqueue(child)
        return False

    def breadth_first_traversal(self):
        if self.is_empty(): return []
        data = []
        queue = Queue()
        queue.enqueue(self._root)
        while not queue.is_empty():
            current = queue.dequeue()
            data.append(current.data)
            for child in current.children:
                queue.enqueue(child)
        return data

    def dfs_pre_order(self):
        if self.is_empty(): return []
        data = []
        # A list is used instead of a true stack because indexing is needed to access the children
        stack = []
        visited = set()
        data.append(self._root.data)
        stack.append(self._root)
        visited.add(self._root)
        while len(stack) > 0:
            all_children_visited = True

            # If the top of the stack is a leaf node, remove it from the stack
            if len(stack[-1].children) == 0:
                stack.pop()
            else:
                parent = stack[-1]

            for child in parent.children:
                if child not in visited:
                    all_children_visited = False
                    data.append(child.data)
                    stack.append(child)
                    visited.add(child)
                    break # Only add one child at a time

            # If all child nodes have been visited, remove the parent from the stack
            if all_children_visited:
                stack.pop()

        return data

    def dfs_in_order(self):
        if self.is_empty(): return []
        data = []
        # A list is used instead of a true stack because indexing is needed to access the children
        stack = []
        visited = set()
        stack.append(self._root)
        while len(stack) > 0:
            all_children_visited = True
            # If the top of the stack is a leaf node, add it to data and remove it from the stack
            if len(stack[-1].children) == 0:
                current = stack[-1]
                data.append(current.data)
                visited.add(current)
                stack.pop()
            else:
                parent = stack[-1]
                child_count = len(parent.children)

            for index, child in enumerate(parent.children):
                # Add the parent after the first half of child nodes have been visited
                if (parent not in visited and
                    (child_count == 2 and index == 1 or
                    child_count > 2 and index == child_count // 2 + 1)):
                    data.append(parent.data)
                    visited.add(parent)
                if child not in visited:
                    all_children_visited = False
                    stack.append(child)
                    break # Only add one child at a time

            # If all child nodes have been visited, remove the parent from the stack and add it to the data
            if all_children_visited:
                stack.pop()

        return data

    def dfs_post_order(self):
        if self.is_empty(): return []
        data = []
        # A list is used instead of a true stack because indexing is needed to access the children
        stack = []
        visited = set()
        stack.append(self._root)
        visited.add(self._root)
        while len(stack) > 0:
            all_children_visited = True

            # If the top of the stack is a leaf node, add it to data and remove it from the stack
            if len(stack[-1].children) == 0:
                current = stack[-1]
                data.append(current.data)
                stack.pop()
            else:
                parent = stack[-1]

            for child in parent.children:
                if child not in visited:
                    all_children_visited = False
                    stack.append(child)
                    visited.add(child)
                    break # Only add one child at a time

            # If all child nodes have been visited, remove the parent from the stack and add it to the data
            if all_children_visited:
                parent = stack.pop()
                data.append(parent.data)

        return data
