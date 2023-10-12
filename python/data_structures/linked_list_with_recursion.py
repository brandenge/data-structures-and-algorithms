from data_structures.node import Node

class LinkedListWithRecursion:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None and self._tail is None

    def count(self, data = None):
        if self.is_empty(): return 0
        return self._head.count(data)

    def append(self, data):
        node = Node(data)
        if self.is_empty(): self._head = node
        else: self._tail.next = node
        self._tail = node
        return data

    def prepend(self, data):
        node = Node(data)
        node.next = self._head
        self._head = node
        if self._tail is None: self._tail = node
        return data

    def find_by_index(self, index):
        if self.is_empty(): return
        if index < 0 or index >= self.count(): return
        return self._head.find_by_index(index)

    def find_index_of(self, data):
        if self.is_empty(): return
        return self._head.find_index_of(data)

    def to_array(self):
        print('self is none: ', self is None)
        if self.is_empty(): return []
        return self._head.to_array([])

    def __str__(self):
        return ' -> '.join(map(str, self.to_array()))
  
    def insert_at_index(self, index, data):
        if index == 0: return self.prepend(data)
        if index == self.count(): return self.append(data)
        if index < 0 or index > self.count(): return
        self._head.insert_at_index(index, data)
        return data

    def _get_previous_node_by_index(self, index):
        if index < 1 or index >= self.count() or self.is_empty(): return
        return self._head._get_previous_node_by_index(index)

    def delete_at_index(self, index):
        if index < 0 or index >= self.count() or self.is_empty(): return
        if index == 0:
            deleted_node = self._head
            self._head = self._head.next
            if self._head is None: self._tail = None # The list is now empty
            return deleted_node.data
        prev_node = self._get_previous_node_by_index(index)
        deleted_node = prev_node.next
        prev_node.next = prev_node.next.next
        if self._tail == deleted_node: self._tail = prev_node
        if self.count() == 0:
            self._head = None
            self._tail = None
        return deleted_node.data

    def delete_data(self, data):
        index = self.find_index_of(data)
        if index is None: return None
        return self.delete_at_index(index)

    def insert_list(self, index, list):
        if list.is_empty() or self.is_empty() or index < 0 or index > self.count(): return self
        if index == 0:
            list._tail.next = self._head
            self._head = list._head
            return self
        if index == self.count():
            self._tail.next = list._head
            self._tail = list._tail
            return self
        
        prev_node = self._get_previous_node_by_index(index)
        next_node = prev_node.next
        prev_node.next = list._head
        list._tail.next = next_node
        return self

    def reverse(self):
        if self.count() < 2: return self
        self._head.reverse(None)
        self._head, self._tail = self._tail, self._head
        return self
  
    def sort(self):
        array = self.to_array()
        array.sort()
        list = self.__class__()
        for element in array:
            list.append(element)
        return list
