from data_structures.node import Node
    
class Stack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def peek(self):
        return (None if self.is_empty() else self._top.data)
    
    def count(self):
        if self.is_empty(): return 0
        return self._top.count()
    
    def push(self, data):
        node = Node(data)
        node.next = self._top
        self._top = node
        return data

    def pop(self):
        if self.is_empty(): return
        temp = self._top
        self._top = self._top.next
        return temp.data