# Binary Tree, Binary Search Tree, and K-ary Tree Implementations

These are implementations of a binary tree, binary search tree, and k-ary tree along with class methods for depth-first traversal methods, adding nodes, and checking if they contain a node with a certain value.

[Link to Code](./index.js)

## Challenge

- Create a `BinaryNode` class with `value`, `left`, and `right` properties.
- Create a `BinaryTree` class with `preOrder`, `inOrder`, and `postOrder` methods.
- Create a `BinarySearchTree` class with `add` and `contains` methods.
- Create a `KaryNode` class with `value` and `children` properties.
- Create a `KaryTree` class with `preOrder`, `inOrder`, and `postOrder` methods.

## Approach & Efficiency

### Binary Tree

preOrder

- Time complexity: linear O(n)
- Space complexity: linear O(n)

inOrder

- Time complexity: linear O(n)
- Space complexity: linear O(n)

postOrder

- Time complexity: linear O(n)
- Space complexity: linear O(n)

### Binary Search Tree

add

- Time complexity: linear O(n)
- Space complexity: constant O(1)

contains

- Time complexity: linear O(n)
- Space complexity: constant O(1)

### K-ary Tree

preOrder

- Time complexity: linear O(n)
- Space complexity: linear O(n)

inOrder

- Time complexity: linear O(n)
- Space complexity: linear O(n)

postOrder

- Time complexity: linear O(n)
- Space complexity: linear O(n)

## API

### Binary Tree API

preOrder

- Argument: none.
- Returns: returns an array of node values in order of pre-order, depth-first traversal.
- Side effects: none.

inOrder

- Argument: none.
- Returns: returns an array of node values in order of in-order, depth-first traversal.
- Side effects: none.

postOrder

- Argument: none.
- Returns: returns an array of node values in order of post-order, depth-first traversal.
- Side effects: none.

### Binary Search Tree API

add

- Argument: a value to insert.
- Returns: nothing.
- Side effects: creates a new node with the provided value, and inserts it sorted order in the binary search tree.

contains

- Argument: a value to search for.
- Returns: a boolean representing whether the value exists inside of the binary search tree.
- Side effects: none.

### K-ary Tree API

preOrder

- Argument: none.
- Returns: returns an array of node values in order of pre-order, depth-first traversal.
- Side effects: none.

inOrder

- Argument: none.
- Returns: returns an array of node values in order of in-order, depth-first traversal.
- Side effects: none.

postOrder

- Argument: none.
- Returns: returns an array of node values in order of post-order, depth-first traversal.
- Side effects: none.
