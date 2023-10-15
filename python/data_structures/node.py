class Node:
    def __init__(self, data = None):
        self._data = data
        self.next = None
        self.left = None
        self.right = None

    @property
    def data(self):
        return self._data
    
    def count(self, data = None):
        if data is None: 
            if self.next is None: return 1
            return 1 + self.next.count(data)
        else:
            if self.next is None: return (1 if self.data == data else 0)
            return (1 if self.data == data else 0) + self.next.count(data)
        
    def find_by_index(self, index):
        if index == 0: return self.data
        return self.next.find_by_index(index - 1)
    
    def find_index_of(self, data, index = 0):
        if self.data == data: return index
        if self.next is None: return
        return self.next.find_index_of(data, index + 1)
    
    def to_array(self, array):
        array += [self.data]
        if self.next is None: return array
        return self.next.to_array(array)
    
    def insert_at_index(self, index, data):
        if index == 1:
            node = Node(data)
            next = self.next
            self.next = node
            node.next = next
            return data
        return self.next.insert_at_index(index - 1, data)

    def _get_previous_node_by_index(self, index):
        if index == 1: return self
        return self.next._get_previous_node_by_index(index - 1)
    
    def reverse(self, prev):
        next = self.next
        self.next = prev
        if next is None: return
        return next.reverse(self)
