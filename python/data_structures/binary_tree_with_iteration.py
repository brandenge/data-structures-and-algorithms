from data_structures.node import Node
from data_structures.queue import Queue
from data_structures.stack import Stack

class BinaryTreeWithIteration:
    def __init__(self):
        self._root = None

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
            if not current.left: 
                current.left = node
                return data
            elif not current.right:
                current.right = node
                return data
            else:
                if current.left: queue.enqueue(current.left)
                if current.right: queue.enqueue(current.right)

    def includes(self, data):
        if self.is_empty(): return False
        queue = Queue()
        queue.enqueue(self._root)
        while not queue.is_empty():
            current = queue.dequeue()
            if current.data == data: return True
            if current.left: queue.enqueue(current.left)
            if current.right: queue.enqueue(current.right)
        return False

    def breadth_first_traversal(self):
        if self.is_empty(): return []
        data = []
        queue = Queue()
        queue.enqueue(self._root)
        while not queue.is_empty():
            current = queue.dequeue()
            data.append(current.data)
            if current.left: queue.enqueue(current.left)
            if current.right: queue.enqueue(current.right)
        return data
    
    def dfs_pre_order(self):
        if self.is_empty(): return []
        data = []
        stack = Stack()
        current = self._root
        while not stack.is_empty() or current:
            # Find the left-most node
            if current:
                data.append(current.data)
                stack.push(current)
                current = current.left
            # After we reach the left-most node
            else:
                prev = stack.pop()
                current = prev.right
        return data

    def dfs_pre_order_alternative(self):
        if self.is_empty(): return []
        data = []
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            current = stack.pop()
            data.append(current.data)
            if current.right: stack.push(current.right)
            if current.left: stack.push(current.left)
        return data

    def dfs_in_order(self):
        if self.is_empty(): return []
        data = []
        stack = Stack()
        current = self._root
        while not stack.is_empty() or current:
            # Find the left-most node
            if current:
                stack.push(current)
                current = current.left
            # After we reach the left-most node
            else:
                prev = stack.pop()
                data.append(prev.data)
                current = prev.right
        return data
    
    def dfs_post_order(self):
        # Note the use of current is the only thing that traverses the tree downward only
        # The stack is what is used to traverse across and up the tree

        if self.is_empty(): return []
        data = []
        stack = Stack()
        current = self._root
        while True:
            # Only use current to navigate down the tree
            # Once all the sub-tree's nodes are added to the stack, set current to None
            while current:
                if current.right: stack.push(current.right)
                stack.push(current)
                current = current.left

            if stack.is_empty(): return data
            current = stack.pop()
    
            if current.right and current.right == stack.peek():
                # Reverse the ordering on the stack so that current will be in front of its right child
                # Current right child is first removed, to be added back in the above loop
                stack.pop()
                stack.push(current)
                current = current.right
                continue

            data.append(current.data)
            # Done traversing this sub-tree, so set current to None
            current = None

    def dfs_post_order_two_stacks(self):
        if self.is_empty(): return []
        data = []
        stack1 = Stack()
        stack2 = Stack()
        stack1.push(self._root)
        # Similar to the reverse sequence of pre-order DFS, left before right instead of right before left
        while not stack1.is_empty():
            current = stack1.pop()
            stack2.push(current)
            if current.left: stack1.push(current.left)
            if current.right: stack1.push(current.right)
        while not stack2.is_empty():
            current = stack2.pop()
            data.append(current.data)
        return data
