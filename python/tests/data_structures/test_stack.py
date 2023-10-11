import pytest
from data_structures.stack import Stack, Node

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
        
class TestStack:
    @pytest.fixture
    def stack(self):
        return Stack()
    
    def test_exists(self, stack):
        assert stack

    def test_initialization(self, stack):
        assert stack.peek() is None
        assert stack.count() == 0

    def test_is_empty(self, stack):
        assert stack.is_empty()
        stack.push(5)
        assert not stack.is_empty()
        stack.pop()
        assert stack.is_empty()

    def test_peek(self, stack):
        assert stack.is_empty()
        assert stack.peek() is None
        stack.push(1)
        assert stack.peek() == 1
        stack.push(2)
        assert stack.peek() == 2
        stack.push(3)
        assert stack.peek() == 3
        stack.pop()
        assert stack.peek() == 2
        stack.pop()
        assert stack.peek() == 1
        stack.pop()
        assert stack.peek() is None
        assert stack.is_empty()

    def test_length(self, stack):
        assert stack.is_empty()
        assert stack.count() == 0
        stack.push(1)
        assert stack.count() == 1
        stack.push(2)
        assert stack.count() == 2
        stack.push(3)
        assert stack.count() == 3
        stack.pop()
        assert stack.count() == 2
        stack.pop()
        assert stack.count() == 1
        stack.pop()
        assert stack.count() == 0
        assert stack.is_empty()

    def test_push(self, stack):
        assert stack.is_empty()
        assert stack.peek() is None
        assert stack.count() == 0
        assert stack.push(1) == 1
        assert stack.peek() == 1
        assert stack.count() == 1
        assert stack.push(2) == 2
        assert stack.peek() == 2
        assert stack.count() == 2
        assert stack.push(3) == 3
        assert stack.peek() == 3
        assert stack.count() == 3

    def test_pop(self, stack):
        assert stack.is_empty()
        assert stack.peek() is None
        assert stack.pop() is None
        assert stack.count() == 0
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.peek() == 3
        assert stack.count() == 3
        assert stack.pop() == 3
        assert stack.peek() == 2
        assert stack.count() == 2
        assert stack.pop() == 2
        assert stack.peek() == 1
        assert stack.count() == 1
        assert stack.pop() == 1
        assert stack.peek() is None
        assert stack.count() == 0
        assert stack.is_empty()
        assert stack.pop() is None
