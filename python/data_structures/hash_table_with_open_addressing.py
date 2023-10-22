from data_structures.node import Node
from functools import reduce

class HashTableWithOpenAddressing:
    def __init__(self, size):
        self._size = size
        self._table = [None] * size
        self._keys = []

    def keys(self):
        return self._keys

    def has(self, key):
        return key in self._keys

    def is_full(self):
      return len(self._keys) >= self._size

    def double_hash(self, key):
        ascii_values = [*map(ord, [*key])]
        total = sum(ascii_values)
        hash = total * len(key)
        return hash

    def hash(self, key):
        ascii_values = [*map(ord, [*key])]
        sum = reduce(lambda sum, n: sum + pow(n, 2), ascii_values)
        hash_index = sum * pow(len(key), 2) % self._size
        bucket = self._table[hash_index]
        counter = 1
        step = self.double_hash(key)
        while True:
            if bucket is None or bucket.key == key or self.is_full():
                return hash_index
            hash_index = (hash_index + step * counter) % self._size
            bucket = self._table[hash_index]
            counter += 1

    def set(self, key, value):
        hash_index = self.hash(key)
        key_value = self._table[hash_index]
        if self.is_full(): self._keys.remove(key_value.key)
        key_value = Node(value)
        key_value.key = key
        self._table[hash_index] = key_value
        self._keys.append(key)
        return value

    def get(self, key):
        if not self.has(key): return
        hash_index = self.hash(key)
        bucket = self._table[hash_index]
        return bucket.value

    def remove(self, key):
        if not self.has(key): return
        hash_index = self.hash(key)
        self._table[hash_index] = None
        self._keys.remove(key)

    def re_size(self, new_size):
        keys = self.keys()
        new_hash_table = HashTableWithOpenAddressing(new_size)
        for key in keys:
            new_hash_table.set(key, self.get(key))
        return new_hash_table
