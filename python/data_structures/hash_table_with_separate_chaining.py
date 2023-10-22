from data_structures.linked_list_with_iteration import LinkedListWithIteration as LinkedList
from functools import reduce

class HashTableWithSeparateChaining:
    def __init__(self, size):
        self._size = size
        self._table = [None] * size
        self._keys = []

    def hash(self, key):
        ascii_values = [*map(ord, [*key])]
        sum = reduce(lambda sum, n: sum + pow(n, 2), ascii_values)
        hash = sum * pow(len(key), 2) % self._size
        return hash

    def set(self, key, value):
        hash_index = self.hash(key)
        bucket = self._table[hash_index]
        if bucket is None: bucket = LinkedList()
        bucket.add_hash_key_value(key, value)
        self._table[hash_index] = bucket
        self._keys.append(key)
        return value

    def keys(self):
        return self._keys

    def has(self, key):
        return key in self._keys

    def get(self, key):
        if not self.has(key): return
        hash_index = self.hash(key)
        bucket = self._table[hash_index]
        return bucket.get_hash_key_value(key)

    def remove(self, key):
        if not self.has(key): return
        hash_index = self.hash(key)
        bucket = self._table[hash_index]
        bucket.remove_hash_key_value(key)
        self._keys.remove(key)

    def re_size(self, new_size):
        new_hash_table = HashTableWithSeparateChaining(new_size)
        for key in self._keys:
            new_hash_table.set(key, self.get(key))
        return new_hash_table

    def left_join(self, hash_table):
        for key in hash_table.keys():
            self.set(key, hash_table.get(key))
        return self
