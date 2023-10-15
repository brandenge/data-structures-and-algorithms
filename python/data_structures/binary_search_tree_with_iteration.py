from data_structures.node import Node
from data_structures.queue import Queue
from data_structures.binary_tree_with_iteration import BinaryTreeWithIteration

class BinarySearchTreeWithIteration(BinaryTreeWithIteration):
    def __init__(self):
        super().__init__()
    
    def add(self, value):
        node = Node(value)
        if self.is_empty():
            self._root = node
            return value
        queue = Queue()
        queue.enqueue(self._root)
        while not queue.is_empty():
            current = queue.dequeue()
            if value <= current.data:
                if current.left: 
                    queue.enqueue(current.left)
                else:
                    current.left = node
                    return value
            else:
                if current.right:
                    queue.enqueue(current.right)
                else:
                    current.right = node
                    return value

    def includes(self, value):
        if self.is_empty(): return False
        queue = Queue()
        queue.enqueue(self._root)
        while not queue.is_empty():
            current = queue.dequeue()
            if value == current.data: return True
            if value < current.data and current.left: queue.enqueue(current.left)
            elif value > current.data and current.right: queue.enqueue(current.right)
        return False
