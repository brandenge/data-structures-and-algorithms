from data_structures.hash_table_with_open_addressing import HashTableWithOpenAddressing as HashTable

def test_initialization():
    assert HashTable(100)

def test_keys():
    hash_table = HashTable(100)
    assert hash_table.keys() == []
    hash_table.set('a', 1)
    assert hash_table.keys() == ['a']
    hash_table.set('b', 2)
    assert hash_table.keys() == ['a', 'b']
    hash_table.set('c', 3)
    assert hash_table.keys() == ['a', 'b', 'c']

def test_has():
    hash_table = HashTable(100)
    assert hash_table.has('abc') is False
    hash_table.set('abc', 123)
    assert hash_table.has('abc') is True

def test_is_full():
    hash_table = HashTable(3)
    assert hash_table.is_full() is False
    assert hash_table.set('a', 1)
    assert hash_table.is_full() is False
    assert hash_table.set('b', 2)
    assert hash_table.is_full() is False
    assert hash_table.set('c', 3)
    assert hash_table.is_full() is True
    assert hash_table.set('d', 4)
    assert hash_table.is_full() is True

def test_set_and_get_happy():
    hash_table = HashTable(100)
    assert hash_table.set('a', 1) == 1
    assert hash_table.get('a') == 1
    assert hash_table.set('b', 2) == 2
    assert hash_table.get('b') == 2
    assert hash_table.set('c', 3) == 3
    assert hash_table.get('c') == 3
    assert hash_table.set('abc', 123) == 123
    assert hash_table.get('abc') == 123

def test_get_sad():
    hash_table = HashTable(100)
    assert hash_table.get('abc') is None

def test_remove():
    hash_table = HashTable(100)
    assert hash_table.remove('a') is None
    hash_table.set('a', 1)
    hash_table.set('b', 2)
    hash_table.set('c', 3)
    assert hash_table.keys() == ['a', 'b', 'c']
    assert hash_table.remove('b') is None
    assert hash_table.keys() == ['a', 'c']
    assert hash_table.remove('a') is None
    assert hash_table.keys() == ['c']
    assert hash_table.remove('c') is None
    assert hash_table.keys() == []

def test_re_size():
    hash_table = HashTable(100)
    hash_table.set('a', 1)
    hash_table.set('b', 2)
    hash_table.set('c', 3)
    new_hash_table = hash_table.re_size(1000)
    assert new_hash_table.get('a') == 1
    assert new_hash_table.get('b') == 2
    assert new_hash_table.get('c') == 3

def test_collision_resolution():
    hash_table = HashTable(1)
    assert hash_table.set('a', 1) == 1
    assert hash_table.get('a') == 1
    assert hash_table.keys() == ['a']
    assert hash_table.set('b', 2) == 2
    assert hash_table.get('b') == 2
    assert hash_table.get('a') is None
    assert hash_table.keys() == ['b']
    assert hash_table.set('c', 3) == 3
    assert hash_table.get('c') == 3
    assert hash_table.get('b') is None
    assert hash_table.get('a') is None
    assert hash_table.keys() == ['c']

def test_probe_sequence():
    hash_table = HashTable(3)
    assert hash_table.set('a', 1) == 1
    assert hash_table.get('a') == 1
    assert hash_table.keys() == ['a']
    assert hash_table.set('b', 2) == 2
    assert hash_table.get('b') == 2
    assert hash_table.get('a') == 1
    assert hash_table.keys() == ['a', 'b']
    assert hash_table.set('c', 3) == 3
    assert hash_table.get('c') == 3
    assert hash_table.get('b') == 2
    assert hash_table.get('a') == 1
    assert hash_table.keys() == ['a', 'b', 'c']
    assert hash_table.set('d', 4) == 4
    assert hash_table.get('d') == 4
    assert hash_table.get('c') == 3
    assert hash_table.get('b') == 2
    assert hash_table.get('a') is None
    assert hash_table.keys() == ['b', 'c', 'd']

def test_left_join():
    hash_table1 = HashTable(100)
    hash_table2 = HashTable(10)
    hash_table1.set('abc', 123)
    hash_table2.set('a', 1)
    hash_table2.set('b', 2)
    hash_table2.set('c', 3)
    hash_table1.left_join(hash_table2)
    assert hash_table1.get('abc') == 123
    assert hash_table1.get('a') == 1
    assert hash_table1.get('b') == 2
    assert hash_table1.get('c') == 3
