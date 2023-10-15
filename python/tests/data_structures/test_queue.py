import pytest
from data_structures.queue import Queue

@pytest.fixture
def queue():
    return Queue()

def test_exists(queue):
    assert queue

def test_initialization(queue):
    assert queue.peek() is None
    assert queue.count() == 0

def test_is_empty(queue):
    assert queue.is_empty()
    queue.enqueue(5)
    assert not queue.is_empty()
    queue.dequeue()
    assert queue.is_empty()

def test_count(queue):
    assert queue.is_empty()
    assert queue.count() == 0
    queue.enqueue(1)
    assert queue.count() == 1
    queue.enqueue(2)
    assert queue.count() == 2
    queue.enqueue(3)
    assert queue.count() == 3
    queue.dequeue()
    assert queue.count() == 2
    queue.dequeue()
    assert queue.count() == 1
    queue.dequeue()
    assert queue.count() == 0
    assert queue.is_empty()

def test_peek(queue):
    assert queue.is_empty()
    assert queue.peek() is None
    queue.enqueue(1)
    assert queue.peek() == 1
    queue.enqueue(2)
    assert queue.peek() == 1
    queue.enqueue(3)
    assert queue.peek() == 1
    queue.dequeue()
    assert queue.peek() == 2
    queue.dequeue()
    assert queue.peek() == 3
    queue.dequeue()
    assert queue.peek() is None

def test_enqueue(queue):
    assert queue.to_array() == []
    assert queue.enqueue(1) == 1
    assert queue.to_array() == [1]
    assert queue.enqueue(2) == 2
    assert queue.to_array() == [1, 2]
    assert queue.enqueue(3) == 3
    assert queue.to_array() == [1, 2, 3]

def test_dequeue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.to_array() == [1, 2, 3]
    assert queue.dequeue() == 1
    assert queue.to_array() == [2, 3]
    assert queue.dequeue() == 2
    assert queue.to_array() == [3]
    assert queue.dequeue() == 3
    assert queue.to_array() == []
    assert queue.dequeue() is None
    assert queue.to_array() == []

def test_to_array(queue):
    assert queue.to_array() == []
    queue.enqueue(1)
    assert queue.to_array() == [1]
    queue.enqueue(2)
    assert queue.to_array() == [1, 2]
    queue.enqueue(3)
    assert queue.to_array() == [1, 2, 3]