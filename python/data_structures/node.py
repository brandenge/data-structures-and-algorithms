class Node:
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

    def count(self, data = None):
        if data is None: 
            if self._next is None: return 1
            return 1 + self._next.count(data)
        else:
            if self._next is None: return (1 if self.data == data else 0)
            return (1 if self.data == data else 0) + self._next.count(data)
        
    def find_by_index(self, index):
        if index == 0: return self.data
        return self._next.find_by_index(index - 1)
    
    def find_index_of(self, data, index = 0):
        if self.data == data: return index
        if self._next is None: return
        return self._next.find_index_of(data, index + 1)
    
    def to_array(self, array):
        array += [self.data]
        if self._next is None: return array
        return self._next.to_array(array)
    
    def insert_at_index(self, index, data):
        if index == 1:
            node = Node(data)
            next = self._next
            self._next = node
            node._next = next
            return data
        return self._next.insert_at_index(index - 1, data)

    def _get_previous_node_by_index(self, index):
        if index == 1: return self
        return self._next._get_previous_node_by_index(index - 1)
    
    def reverse(self, prev):
        next = self._next
        self._next = prev
        if next is None: return
        return next.reverse(self)
