import pytest
from data_structures.queue import Queue, Node

class TestNode:
    @pytest.fixture
    def node(self):
        return Node()

    def test_exists(self, node):
        assert node

    def initialization(self, node):
        assert node.data == None
        assert node.next == None

        node = Node(5)
        assert node.data == 5
        assert node.next == None
        
class TestQueue:
    @pytest.fixture
    def queue(self):
        return Queue()
    
    def test_exists(self, queue):
        assert queue

    def test_initialization(self, queue):
        assert queue.peek() is None
        assert queue.count() == 0

    def test_is_empty(self, queue):
        assert queue.is_empty()
        queue.enqueue(5)
        assert not queue.is_empty()
        queue.dequeue()
        assert queue.is_empty()

    def test_length(self, queue):
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

    def test_peek(self, queue):
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

    def test_enqueue(self, queue):
        assert queue.peek() is None
        assert queue.count() == 0
        assert queue.enqueue(1) == 1
        assert queue.peek() == 1
        assert queue.count() == 1
        assert queue.enqueue(2) == 2
        assert queue.peek() == 1
        assert queue.count() == 2
        assert queue.enqueue(3) == 3
        assert queue.peek() == 1
        assert queue.count() == 3

    def test_dequeue(self, queue):
        assert queue.dequeue() is None
        assert queue.count() == 0
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.count() == 3
        assert queue.peek() == 1
        assert queue.dequeue() == 1
        assert queue.count() == 2
        assert queue.peek() == 2
        assert queue.dequeue() == 2
        assert queue.count() == 1
        assert queue.peek() == 3
        assert queue.dequeue() == 3
        assert queue.count() == 0
        assert queue.peek() is None
        assert queue.dequeue() is None
        assert queue.count() == 0
