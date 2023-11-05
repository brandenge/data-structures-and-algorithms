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

    # Standard implementation that swaps the deleted node with the successor node
    def delete(self, value):
        if self.is_empty(): return

        node_to_delete = None
        parent_of_successor_node = None

        if self._root.data > value: successor_node = self._root
        else: successor_node = None

        queue = Queue()
        queue.enqueue(self._root)
        while not queue.is_empty():
            current = queue.dequeue()
            if value == current.data:
                node_to_delete = current
            if current.left:
                if current.left.data > value:
                    if (successor_node is None or
                        current.left.data < successor_node.data):
                        successor_node = current.left
                        parent_of_successor_node = current
                queue.enqueue(current.left)
            if current.right:
                if current.right.data >= value:
                    if (successor_node is None or
                        current.right.data < successor_node.data):
                        successor_node = current.right
                        parent_of_successor_node = current
                queue.enqueue(current.right)
            if queue.is_empty() and successor_node is None:
                successor_node = current

        # if node_to_delete: print('node to delete', node_to_delete.data)
        # else: print('node to delete', node_to_delete)
        # if successor_node: print('successor node', successor_node.data)
        # else: print('successor node', successor_node)
        # if parent_of_successor_node: print('parent of successor node', parent_of_successor_node.data)
        # else: print('parent of successor node', parent_of_successor_node)

        if node_to_delete:
            if not node_to_delete.left and not node_to_delete.right:
                if successor_node.left == node_to_delete:
                    successor_node.left = None
                elif successor_node.right == node_to_delete:
                    successor_node.right = None

                # The node to delete is the right-most leaf node
                # And the successor node is the node to delete
                if parent_of_successor_node and parent_of_successor_node.left == node_to_delete:
                    parent_of_successor_node.left = None
                elif parent_of_successor_node and parent_of_successor_node.right == node_to_delete:
                    parent_of_successor_node.right = None

                # The node to delete is the root node and is the last node in the tree
                elif node_to_delete == self._root: self._root = None

                return value
            node_to_delete.data = successor_node.data
            if parent_of_successor_node.left == successor_node:
                parent_of_successor_node.left = None
            elif parent_of_successor_node.right == successor_node:
                parent_of_successor_node.right = None
            successor_node.left = None
            successor_node.right = None

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
