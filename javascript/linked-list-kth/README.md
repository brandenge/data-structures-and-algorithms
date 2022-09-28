# Singly Linked List

This is an implementation of a linked list data structure along with a variety of methods for manipulating the linked list.

## Challenge

- Create a Node class with `value` and `next` properties.
- Create a LinkedList class with a `head` property, and `insert`, `includes`, `toString`, `append`, `insertBefore`, `insertAfter`, `delete`, `kthFromEnd`, and `getMiddleNodeValue` methods.
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

append:

- Constant O(1) time complexity because I am using a tail pointer to the last node of the list so there is no while loop needed to traverse the list for this append operation.
- Constant O(1) space complexity because our variables do not grow with the length of the list.

insertBefore:

- Linear O(n) time complexity because we have a while loop to traverse the list.
- Constant O(1) space complexity because our variables do not grow with the length of the list.

insertAfter:

- Linear O(n) time complexity because we have a while loop to traverse the list.
- Constant O(1) space complexity because our variables do not grow with the length of the list.

delete:

- Linear O(n) time complexity because we have a while loop to traverse the list.
- Constant O(1) space complexity because our variables do not grow with the length of the list.

I optimized the append method from a more normal implementation by adding a `tail` property, in addition to `head`, which would always point to the last node and make the append operations to be just as fast as prepend operations. While this does optimize performance from linear O(n) to constant O(1) time complexity and at a negligible cost of extra memory, the real cost of this implementation is the added bloat, complexity, and diminished readability of the code in order to correctly handle the `tail` property in all of the other methods used by the linked list class. While good practice, I would not recommend using such an implementation as this unless there is a need for a significant number of append operations needed to be done on very large linked lists, and the linked list class does not have many other methods that would be affected by the added complexity.

kthFromEnd:

- Linear O(n) time complexity because we have a while loop to traverse the list.
- Constant O(1) space complexity because we are using a fixed number of variables, and each one does not grow in its memory usage with the size of the linked list.

getMiddleNodeValue:

- Linear O(n) time complexity because we have a while loop to traverse the list.
- Constant O(1) space complexity because we are using a fixed number of variables, and each one does not grow in its memory usage with the size of the linked list.

## API

insert:

- Arguments: a value. Takes a single argument which is the value of a new node to be inserted.
- Returns: undefined.

includes:

- Arguments: a value. Takes a single argument which is the value to be searched for.
- Returns: a boolean.
- Returns true if it finds the value inside one of the nodes of the linked list.
- Returns false if it searches all of the nodes in the linked list and did not find the value.

toString:

- Arguments: none. Takes no arguments.
- Returns a formatted string in the format of `"{ a } -> { b } -> { c } -> NULL"`, where `a`, `b`, and `c` are the values of each node in the linked list.
- Traverses the linked list and appends each node's value to a formatted string.

append:

- Arguments: a value. Takes a single argument which is the value of a new node to be appended.
- Returns: nothing.

insertBefore:

- Arguments: two values. The first value is the value of the node that is to be inserted before. The second value is the value of the new node being inserted.
- Returns: nothing.

insertAfter:

- Arguments: two values. The first value is the value of the node that is to be inserted after. The second value is the value of the new node being inserted.
- Returns: nothing.

delete:

- Arguments: a value. Takes a single argument which is the value of the node to be deleted.
- Returns: nothing.

kthFromEnd:

- Arguments: a positive integer. This represents how many nodes from the end of the linked list.
- Returns: The value of the kth node from the end of the linked list, or an error if the argument is not valid.

getMiddleNodeValue:

- Arguments: none.
- Returns: The value of the middle node of the linked list, or an error if the linked list is empty.
