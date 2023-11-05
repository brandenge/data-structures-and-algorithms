from data_structures.node import Node
from data_structures.queue import Queue

# Note that recursive logic is kept here in binary tree class, outside of Node class
# An alternative approach would be to move the recursive logic into the Node class
# Like the LinkedListWithRecursion implementation
class BinaryTreeWithRecursion:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def add(self, data):
        node = Node(data)
        if self.is_empty():
            self._root = node
            return data

        # Need a queue to add using BFS instead of DFS
        queue = Queue()
        queue.enqueue(self._root)

        # Note the use of lexical scope to avoid needing to pass in additional arguments
        def traverse_add():
            if queue.is_empty(): return
            current = queue.dequeue()
            if not current.left:
                current.left = node
                return
            if not current.right:
                current.right = node
                return
            queue.enqueue(current.left)
            queue.enqueue(current.right)
            traverse_add()

        # Note that the queue also enables only a single recursive call being needed here
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
            if current.left: queue.enqueue(current.left)
            if current.right: queue.enqueue(current.right)
            if queue.is_empty(): return [node_to_delete, current]
            return traverse_find_delete_and_last_node()

        return traverse_find_delete_and_last_node()

    def find_parent(self, target):
        if self.is_empty() or target is None: return
        parent_node = None

        def traverse_find_parent(target, current):
            nonlocal parent_node
            if parent_node: return parent_node
            # If the root node is the target, it does not have a parent
            if current.left and current.left == target: parent_node = current
            if current.right and current.right == target: parent_node = current
            if current.left: traverse_find_parent(target, current.left)
            if current.right: traverse_find_parent(target, current.right)

        traverse_find_parent(target, self._root)
        return parent_node

    def delete(self, data):
        if self.is_empty(): return
        # If the root node is the last node in the tree
        if self._root.left is None and self._root.right is None:
            if self._root.data == data:
                self._root = None
                return data
            else:
                return

        node_to_delete, last_node = self.find_node_to_delete_and_last_node(data)
        if node_to_delete is None: return
        parent_of_last_node = self.find_parent(last_node)
        node_to_delete.data = last_node.data
        if parent_of_last_node.left == last_node:
            parent_of_last_node.left = None
        elif parent_of_last_node.right == last_node:
            parent_of_last_node.right = None
        return data

    def includes(self, data):
        if self.is_empty(): return False
        is_included = False

        def traverse_includes(current):
            if current.data == data:
                nonlocal is_included
                is_included = True
                return
            if current.left: traverse_includes(current.left)
            if current.right: traverse_includes(current.right)

        traverse_includes(self._root)
        return is_included

    def breadth_first_traversal(self):
        if self.is_empty(): return []

        # Need a queue to do BFS recursively
        queue = Queue()
        queue.enqueue(self._root)
        data = []

        def traverse_bfs():
            if queue.is_empty(): return
            current = queue.dequeue()
            data.append(current.data)
            if current.left: queue.enqueue(current.left)
            if current.right: queue.enqueue(current.right)

            # Note that the queue also enables only a single recursive call being needed here
            traverse_bfs()

        traverse_bfs()
        return data

    def dfs_pre_order(self):
        if self.is_empty(): return []
        data = []

        def traverse_dfs_pre_order(current):
            if current is None: return
            data.append(current.data)
            traverse_dfs_pre_order(current.left)
            traverse_dfs_pre_order(current.right)

        traverse_dfs_pre_order(self._root)
        return data

    def dfs_in_order(self):
        if self.is_empty(): return []
        data = []

        def traverse_dfs_in_order(current):
            if current is None: return
            traverse_dfs_in_order(current.left)
            data.append(current.data)
            traverse_dfs_in_order(current.right)

        traverse_dfs_in_order(self._root)
        return data

    def dfs_post_order(self):
        if self.is_empty(): return []
        data = []

        def traverse_dfs_post_order(current):
            if current is None: return
            traverse_dfs_post_order(current.left)
            traverse_dfs_post_order(current.right)
            data.append(current.data)

        traverse_dfs_post_order(self._root)
        return data

    def find_height(self, current = 'root'):
        if self.is_empty(): return 0
        if current is None: return 0
        if current == 'root': current = self._root
        left_height = self.find_height(current.left)
        right_height = self.find_height(current.right)
        return max(left_height, right_height) + 1

    def is_balanced(self, current = 'root'):
        if self.is_empty() or current is None: return True
        if current == 'root': current = self._root
        left_height = self.find_height(current.left)
        right_height = self.find_height(current.right)
        if abs(left_height - right_height) <= 1 and self.is_balanced(current.left) and self.is_balanced(current.right):
            return True
        return False
