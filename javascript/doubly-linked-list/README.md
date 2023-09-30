# Doubly Linked List

This is an implementation of a doubly linked list data structure and some basic methods with it.

## Challenge

- Create a Node class with `value`, `next`, and `prev` properties.
- Create a DoublyLinkedList class with a `head` property, and `insert`, `includes`, and `toString` methods.
- Create tests for all classes and methods.

## Approach & Efficiency

insert:

- Constant O(1) time complexity because there is no while loop to traverse the list.
- Constant O(1) space complexity because our variables do not grow with the length of the list.

includes:

- Linear O(n) time complexity because we have a while loop to traverse the list.
- Constant O(1) space complexity because our variables do not grow with the length of the list.

toString:

- Linear O(n) time complexity because we have a while loop to traverse the list.
- Linear O(n) space complexity because our string return value grows in direct proportion to the length of the list.

I prepended any new nodes to the beginning of the linked list for any insertion operations on the linked list. This was per the instructions, but also because this allows for constant O(1) time complexity. Fast insertion operations are a strength of the linked list. If I wanted to add an append method to append a new node to the end of the linked list, I could optimize such an operation by also having a `tail` property, in addition to `head`, which would always point to the last node and make for append operations to be just as fast as prepend operations.

While loops are used to traverse the linked list. We cannot use for loops to traverse a linked list because we do not have any indexes to serve as a kind of "ordered key" for each element, like arrays have.

## API

insert:

- Arguments: value. Takes a single argument which is the value of a new node.
- Returns: undefined.
- Creates a new node.
- Prepends the new node to the beginning (at the head) of the list with O(1) Time performance.
- Updates the old head's prev property to point to the new node (which is the new head).
- Updates the list's head property to point to the newly inserted node.

includes:

- Arguments: value. Takes a single argument which is the value to be searched for.
- Returns: a boolean.
- Returns true if it finds the value inside one of the nodes of the linked list.
- Returns false if it searches all of the nodes in the linked list and did not find the value.
- Traverses the list performing a strict comparison of each node's value.
- Shortcircuits out of the traversal and returns true once it has found the value.

toString:

- Arguments: none. Takes no arguments.
- Returns a formatted string in the format of `"NULL <- { a } ->  <- { b } ->  <- { c } -> NULL"`, where `a`, `b`, and `c` are the values of each node in the doubly linked list.
- Traverses the linked list and appends each node's value to a formatted string.
