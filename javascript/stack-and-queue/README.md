# Stacks and Queues

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue.

## Challenge

- Create a `Node` class with `value` and `next` properties.
- Create a `Stack` class with a `top` property, and write class instance methods for `push`, `pop`, `peek`, and `isEmpty`.
- Create a `Queue` class with `front` and `back` properties, and write class instance methods for `enqueue`, `dequeue`, `peek`, and `isEmpty`.
- Create tests for all methods and pass all tests.

## Approach & Efficiency

push and enqueue

- Time and Space Complexity: O(1).

pop and dequeue

- Time and Space Complexity: O(1).

peek

- Time and Space Complexity: O(1).

isEmpty

- Time and Space Complexity: O(1).

## API

push and enqueue

- Argument: a value.
- Returns: nothing.
- Side effects: adds a node with a value to the top/back of the stack/queue, respectively.

pop and dequeue

- Argument: nothing.
- Returns: the value at the top/front of the stack/queue, respectively.
- Side effects: Removes the top/front node from the stack/queue, respectively.

peek

- Argument: nothing.
- Returns: the value at the top/front of the stack/queue, respectively.
- Side effects: none.

isEmpty

- Argument: nothing.
- Returns: a boolean, true if the stack/queue is empty, or false otherwise.
- Side effects: none.
