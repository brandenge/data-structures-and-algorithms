# Tree Intersection

This is an implementation of a function that finds the shared common values (i.e. an intersection) of two binary trees.

[Link to Code](./tree-intersection.js)

## Challenge

Write a function called treeIntersection that takes two binary trees as parameters. Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

## Approach & Efficiency

Time complexiy - Linear O(n)
Space complexity - Linear O(n)

## API

treeIntersection

- Arguments: two binary trees
- Return: an array of common values shared by both binary trees

## Binary Search Trees

If the trees were binary search trees (BSTs), then I know that the values are sorted if I traverse the BSTs using in-order depth first traversal. This would allow the implemenetation to be optimized by shortcircuiting the traversal of the second BST if it reaches a value that is greater than the maximum value (which is at the very end) of the first BST, or vice-versa.
