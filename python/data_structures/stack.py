class Node():
    def __init__(self, data = None):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, node):
        self._next = node

    def count(self):
        if self._next is None: return 1
        return 1 + self._next.count()
    
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