from data_structures.node import Node
from data_structures.binary_tree_with_recursion import BinaryTreeWithRecursion

class BinarySearchTreeWithRecursion(BinaryTreeWithRecursion):
    def __init__(self):
        super().__init__()

    def add(self, value):
        node = Node(value)
        if self.is_empty():
            self._root = node
            return value

        def traverse_add(current):
            if value <= current.data:
                if not current.left:
                    current.left = node
                    return
                else:
                    traverse_add(current.left)
            else:
                if not current.right:
                    current.right = node
                    return
                else:
                    traverse_add(current.right)

        traverse_add(self._root)
        return value

    def lift_successor(self, successor, node_to_delete):
        # Recursively call the left child to find the successor node
        if successor.left:
            successor.left = self.lift_successor(successor.left, node_to_delete)
            return successor
        else:
            # The successor node is finally found when there is no left child remaining
            # Return the successor's right child to be used as its parent's left child
            node_to_delete.data = successor.data
            return successor.right

    # Note that this version is different from the iterative version in that
    # it returns nodes, not values, and it does not return the deleted value
    def delete(self, value, current = 'None'):
        if self.is_empty(): return
        if current == 'None': current = self._root
        if current is None: return None
        if current.data > value:
            current.left = self.delete(value, current.left)
            return current
        elif current.data < value:
            current.right = self.delete(value, current.right)
            return current
        elif current.data == value:
            if (current == self._root and
                current.left is None and current.right is None):
                self._root = None
                return
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            else:
                # The node to be deleted has 2 children
                # Therefore, we must find the successor and position it correctly
                current.right = self.lift_successor(current.right, current)
                return current

    def includes(self, value):
        if self.is_empty(): return False
        is_included = False

        def traverse_includes(current):
            if value == current.data:
                # This nonlocal declaration is needed because Python does not have the same kind of lexical scope as JavaScript
                nonlocal is_included
                is_included = True
                return
            if value < current.data and current.left: traverse_includes(current.left)
            if value > current.data and current.right: traverse_includes(current.right)

        traverse_includes(self._root)
        return is_included
