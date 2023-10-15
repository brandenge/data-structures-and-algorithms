from data_structures.node import Node
from data_structures.queue import Queue
from data_structures.stack import Stack

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
        
        # Need a queue because I want to add using BFS, not DFS
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

    def includes(self, data):
        if self.is_empty(): return False
        is_included = False

        def traverse_includes(current):
            if current.data == data: is_included = True
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
            data.append(current.data)
            if current.left: traverse_dfs_pre_order(current.left)
            if current.right: traverse_dfs_pre_order(current.right)
        
        traverse_dfs_pre_order(self._root)
        return data

    def dfs_in_order(self):
        if self.is_empty(): return []
        data = []
        
        def traverse_dfs_in_order(current):
            if current.left: traverse_dfs_in_order(current.left)
            data.append(current.data)
            if current.right: traverse_dfs_in_order(current.right)
        
        traverse_dfs_in_order(self._root)
        return data

    def dfs_post_order(self):
        if self.is_empty(): return []
        data = []
        
        def traverse_dfs_post_order(current):
            if current.left: traverse_dfs_post_order(current.left)
            if current.right: traverse_dfs_post_order(current.right)
            data.append(current.data)
        
        traverse_dfs_post_order(self._root)
        return data
