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
    
class Queue():
    def __init__(self):
        self._front = None
        self._back = None

    def is_empty(self):
        return self._front is None and self._back is None
    
    def count(self):
        if self.is_empty(): return 0
        return self._front.count()

    def peek(self):
        return (None if self.is_empty() else self._front.data)
    
    def enqueue(self, data):
        node = Node(data)
        if self.is_empty(): 
            self._front = node
            self._back = node
            return data
        self._back.next = node
        self._back = node
        return data

    def dequeue(self):
        if self.is_empty(): return
        temp = self._front
        if self._front == self._back: self._back = None
        self._front = self._front.next
        return temp.data