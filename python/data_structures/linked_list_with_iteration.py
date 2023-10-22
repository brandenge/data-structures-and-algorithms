from data_structures.node import Node

class LinkedListWithIteration:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None and self._tail is None

    def count(self, data = None):
        if self.is_empty(): return 0
        count_data = 0
        count_total = 0
        current = self._head
        while current:
            if current.data == data: count_data += 1
            count_total += 1
            current = current.next
        return (count_total if data is None else count_data)

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
        current = self._head
        count = 0
        while current:
            if count == index: return current.data
            count += 1
            current = current.next

    def find_index_of(self, data):
        if self.is_empty(): return
        current = self._head
        index = 0
        while current:
            if current.data == data: return index
            index += 1
            current = current.next

    def to_array(self, nodes = False):
        array = []
        current = self._head
        while current:
            if nodes: array.append(current)
            else: array.append(current.data)
            current = current.next
        return array

    def __str__(self):
        return ' -> '.join(map(str, self.to_array()))

    def insert_at_index(self, index, data):
        if index == 0: return self.prepend(data)
        if index == self.count(): return self.append(data)
        if index < 0 or index > self.count(): return
        node = Node(data)
        count = 0
        current = self._head
        while current:
            if count + 1 == index:
                node.next = current.next
                current.next = node
                break
            current = current.next
            count += 1
        return data

    def _get_previous_node_by_index(self, index):
        if index < 1 or index >= self.count() or self.is_empty(): return
        current = self._head
        count = 0
        while current:
            if count + 1 == index: return current
            count += 1
            current = current.next

    def delete_at_index(self, index):
        if index < 0 or index >= self.count() or self.is_empty(): return
        if index == 0:
            deleted_node = self._head
            if self._head.next is None: self._tail = None # The list is now empty
            self._head = self._head.next
            return deleted_node.data
        prev_node = self._get_previous_node_by_index(index)
        deleted_node = prev_node.next
        prev_node.next = prev_node.next.next
        if self._tail == deleted_node: self._tail = prev_node
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
        current = self._head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self._head, self._tail = self._tail, self._head
        return self

    def sort(self):
        array = self.to_array()
        array.sort()
        list = self.__class__()
        for element in array:
            list.append(element)
        return list

    def add_hash_key_value(self, key, value):
        node = Node(value)
        node.key = key
        node.next = self._head
        self._head = node
        if self._tail is None: self._tail = node
        return value

    def get_hash_key_value(self, key):
        current = self._head
        while current:
            if current.key == key: return current.value
            current = current.next

    def get_hash_key_values(self):
        return self.to_array(nodes = True)

    def remove_hash_key_value(self, key):
        if self.is_empty(): return
        if self._head.key == key:
            self._head = self._head.next
            if self._head is None: self._tail = None
            return
        current = self._head
        while current.next:
            if current.next.key == key:
                if current.next is self._tail: current = self._tail
                current.next = current.next.next
                break
            current = current.next
