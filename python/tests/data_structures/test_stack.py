import pytest
from data_structures.stack import Stack

@pytest.fixture
def stack():
    return Stack()

def test_initialization(stack):
    assert stack.peek() is None
    assert stack.count() == 0

def test_is_empty(stack):
    assert stack.is_empty()
    stack.push(5)
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()

def test_peek(stack):
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

def test_count(stack):
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

def test_push(stack):
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

def test_pop(stack):
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

def test_to_array(stack):
    assert stack.to_array() == []
    stack.push(1)
    assert stack.to_array() == [1]
    stack.push(2)
    assert stack.to_array() == [2, 1]
    stack.push(3)
    assert stack.to_array() == [3, 2, 1]
