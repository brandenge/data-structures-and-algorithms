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
