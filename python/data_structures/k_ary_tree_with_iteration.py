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

    # def dfs_in_order(self):
    #     if self.is_empty(): return []
    #     data = []
    #     stack = Stack()
    #     current = self._root
    #     while not stack.is_empty() or current:
    #         # Find the left-most node
    #         if current:
    #             stack.push(current)
    #             current = current.left
    #         # After we reach the left-most node
    #         else:
    #             prev = stack.pop()
    #             data.append(prev.data)
    #             current = prev.right
    #     return data

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
